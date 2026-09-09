"""
MedPredict AI — Patient, Medical Profile & Clinical Assessment Endpoints
"""

from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientRead,
    MedicalProfileUpdate,
    MedicalProfileRead,
    AssessmentCreate,
    AssessmentRead
)
from backend.app.services.patient_service import PatientService
from backend.app.security.deps import (
    get_current_active_user,
    require_roles
)
from backend.app.core.errors import AuthorizationError, EntityNotFoundError
from backend.app.models.user import User

router = APIRouter(prefix="/patients", tags=["Patients & Clinical"])

@router.get("/me", response_model=PatientRead, summary="Get Current Patient Profile")
def get_my_patient_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Retrieves the clinical patient record for the logged-in patient."""
    patient = PatientService.get_by_user_id(db, current_user.id)
    if not patient:
        raise EntityNotFoundError("No patient record associated with current user")
    return patient

@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED, summary="Create Patient Profile")
def create_patient_profile(
    patient_in: PatientCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Creates a patient clinical profile for the current user."""
    return PatientService.create_patient_profile(db, current_user.id, patient_in)

@router.get(
    "/",
    response_model=List[PatientRead],
    summary="List Patients (Doctor & Admin Only)",
    dependencies=[Depends(require_roles("DOCTOR", "ADMIN"))]
)
def list_patients(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """Lists patients for provider review."""
    return PatientService.list_patients(db, skip=skip, limit=limit)

@router.get("/{patient_id}", response_model=PatientRead, summary="Get Patient by ID")
def get_patient(
    patient_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Retrieves a specific patient profile with authorization checks."""
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise EntityNotFoundError(f"Patient '{patient_id}' not found")

    # Authorization: Patient can only view self; Doctors and Admins can view any
    is_self = patient.user_id == current_user.id
    is_staff = any(r.name in ("DOCTOR", "ADMIN") for r in current_user.roles)
    if not (is_self or is_staff):
        raise AuthorizationError("Access denied: You do not have permission to view this patient record")

    return patient

@router.put("/{patient_id}", response_model=PatientRead, summary="Update Patient Demographics")
def update_patient(
    patient_id: str,
    update_in: PatientUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Updates demographic details for a patient."""
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise EntityNotFoundError(f"Patient '{patient_id}' not found")

    is_self = patient.user_id == current_user.id
    is_staff = any(r.name in ("DOCTOR", "ADMIN") for r in current_user.roles)
    if not (is_self or is_staff):
        raise AuthorizationError("Access denied")

    return PatientService.update_patient_profile(db, patient_id, update_in)

@router.put("/{patient_id}/medical-profile", response_model=MedicalProfileRead, summary="Update Medical History")
def update_medical_profile(
    patient_id: str,
    profile_in: MedicalProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Updates medical profile (allergies, chronic conditions, family history)."""
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise EntityNotFoundError(f"Patient '{patient_id}' not found")

    is_self = patient.user_id == current_user.id
    is_staff = any(r.name in ("DOCTOR", "ADMIN") for r in current_user.roles)
    if not (is_self or is_staff):
        raise AuthorizationError("Access denied")

    return PatientService.update_medical_profile(db, patient_id, profile_in)

@router.post("/{patient_id}/assessments", response_model=AssessmentRead, status_code=status.HTTP_201_CREATED, summary="Create Assessment")
def create_assessment(
    patient_id: str,
    assessment_in: AssessmentCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Logs an assessment encounter for a specific disease module."""
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise EntityNotFoundError(f"Patient '{patient_id}' not found")

    is_self = patient.user_id == current_user.id
    is_staff = any(r.name in ("DOCTOR", "ADMIN") for r in current_user.roles)
    if not (is_self or is_staff):
        raise AuthorizationError("Access denied")

    return PatientService.create_assessment(db, patient_id, current_user.id, assessment_in)

@router.get("/{patient_id}/assessments", response_model=List[AssessmentRead], summary="List Patient Assessments")
def list_assessments(
    patient_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Retrieves assessment timeline for a patient."""
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise EntityNotFoundError(f"Patient '{patient_id}' not found")

    is_self = patient.user_id == current_user.id
    is_staff = any(r.name in ("DOCTOR", "ADMIN") for r in current_user.roles)
    if not (is_self or is_staff):
        raise AuthorizationError("Access denied")

    return PatientService.list_assessments(db, patient_id)
