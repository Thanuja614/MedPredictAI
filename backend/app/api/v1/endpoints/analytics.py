"""
MedPredict AI — Analytics Endpoints
Provides routes for longitudinal patient trajectories, cohort population risk
distributions, and clinical platform statistics.
"""

from typing import Optional, Dict, Any
from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.security.deps import get_current_active_user, require_roles
from backend.app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/patient/{patient_id}/timeline")
def get_patient_timeline(
    patient_id: str = Path(..., description="Unique Patient ID"),
    disease_id: Optional[str] = Query(None, description="Optional filter by disease ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Retrieve multi-timepoint longitudinal risk progression and velocity for a patient."""
    return AnalyticsService.get_patient_timeline(db=db, patient_id=patient_id, disease_id=disease_id)

@router.get("/population/distribution")
def get_population_distribution(
    disease_id: Optional[str] = Query(None, description="Optional filter by disease ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "doctor", "researcher", "data_scientist"]))
) -> Dict[str, Any]:
    """Retrieve cohort risk distribution percentiles, summary statistics, and demographic breakdown."""
    return AnalyticsService.get_population_risk_distribution(db=db, disease_id=disease_id)

@router.get("/system-overview")
def get_system_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Retrieve platform aggregate statistics for dashboard rendering."""
    return AnalyticsService.get_system_overview(db=db)
