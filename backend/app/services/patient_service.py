"""
MedPredict AI — Patient & Clinical Domain Service
"""

from typing import List, Optional
from sqlalchemy.orm import Session

from backend.app.models.patient import Patient, MedicalProfile, Assessment
from backend.app.models.disease import Disease
from backend.app.models.audit import AuditLog
from backend.app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    MedicalProfileUpdate,
    AssessmentCreate
)
from backend.app.core.errors import EntityNotFoundError, DataValidationError

class PatientService:

    @staticmethod
    def get_by_id(db: Session, patient_id: str) -> Optional[Patient]:
        return db.query(Patient).filter(Patient.id == patient_id).first()

    @staticmethod
    def get_by_user_id(db: Session, user_id: str) -> Optional[Patient]:
        return db.query(Patient).filter(Patient.user_id == user_id).first()

    @staticmethod
    def list_patients(db: Session, skip: int = 0, limit: int = 50) -> List[Patient]:
        return db.query(Patient).offset(skip).limit(limit).all()

    @staticmethod
    def create_patient_profile(db: Session, user_id: str, patient_in: PatientCreate) -> Patient:
        existing = db.query(Patient).filter(Patient.user_id == user_id).first()
        if existing:
            raise DataValidationError("Patient profile already exists for this user")

        patient = Patient(
            user_id=user_id,
            date_of_birth=patient_in.date_of_birth,
            gender=patient_in.gender,
            blood_group=patient_in.blood_group,
            emergency_contact=patient_in.emergency_contact
        )
        db.add(patient)
        db.flush()

        # Create blank medical profile
        profile = MedicalProfile(patient_id=patient.id)
        db.add(profile)
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def update_patient_profile(db: Session, patient_id: str, update_in: PatientUpdate) -> Patient:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            raise EntityNotFoundError(f"Patient '{patient_id}' not found")

        if update_in.date_of_birth is not None:
            patient.date_of_birth = update_in.date_of_birth
        if update_in.gender is not None:
            patient.gender = update_in.gender
        if update_in.blood_group is not None:
            patient.blood_group = update_in.blood_group
        if update_in.emergency_contact is not None:
            patient.emergency_contact = update_in.emergency_contact

        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def update_medical_profile(db: Session, patient_id: str, profile_in: MedicalProfileUpdate) -> MedicalProfile:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            raise EntityNotFoundError(f"Patient '{patient_id}' not found")

        profile = patient.medical_profile
        if not profile:
            profile = MedicalProfile(patient_id=patient.id)
            db.add(profile)

        if profile_in.allergies is not None:
            profile.allergies = profile_in.allergies
        if profile_in.chronic_conditions is not None:
            profile.chronic_conditions = profile_in.chronic_conditions
        if profile_in.family_history is not None:
            profile.family_history = profile_in.family_history
        if profile_in.lifestyle_notes is not None:
            profile.lifestyle_notes = profile_in.lifestyle_notes

        db.commit()
        db.refresh(profile)
        return profile

    @staticmethod
    def create_assessment(db: Session, patient_id: str, creator_user_id: str, assessment_in: AssessmentCreate) -> Assessment:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            raise EntityNotFoundError(f"Patient '{patient_id}' not found")

        disease = db.query(Disease).filter(Disease.id == assessment_in.disease_id).first()
        if not disease:
            raise EntityNotFoundError(f"Disease '{assessment_in.disease_id}' not found")

        assessment = Assessment(
            patient_id=patient.id,
            created_by_user_id=creator_user_id,
            disease_id=disease.id,
            notes=assessment_in.notes
        )
        db.add(assessment)
        db.flush()

        audit = AuditLog(
            user_id=creator_user_id,
            action="ASSESSMENT_CREATED",
            entity_type="assessments",
            entity_id=assessment.id,
            details_json=f'{{"patient_id": "{patient.id}", "disease_id": "{disease.id}"}}'
        )
        db.add(audit)
        db.commit()
        db.refresh(assessment)
        return assessment

    @staticmethod
    def list_assessments(db: Session, patient_id: str) -> List[Assessment]:
        return db.query(Assessment).filter(Assessment.patient_id == patient_id).order_by(Assessment.created_at.desc()).all()
