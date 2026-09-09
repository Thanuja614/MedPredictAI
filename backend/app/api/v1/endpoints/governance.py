"""
MedPredict AI — Model Governance & Drift Monitoring Endpoints
"""

from typing import Dict, Any, List
from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.security.deps import require_roles
from backend.app.services.governance_service import GovernanceService

router = APIRouter()

@router.get("/models")
def list_governed_models(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist", "doctor"]))
) -> List[Dict[str, Any]]:
    """Lists all registered models, version tags, and lifecycle states (active/staged/archived)."""
    return GovernanceService.list_models_governance(db=db)

@router.post("/models/{version_id}/promote")
def promote_model(
    version_id: str = Path(..., description="Target ModelVersion ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist"]))
) -> Dict[str, Any]:
    """Promotes target model version to ACTIVE champion status and demotes previous active model."""
    return GovernanceService.promote_model_version(db=db, version_id=version_id, user_id=current_user.id)

@router.post("/models/{version_id}/rollback")
def rollback_model(
    version_id: str = Path(..., description="Target ModelVersion ID to restore"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist"]))
) -> Dict[str, Any]:
    """Rollback active production model to specified prior version."""
    return GovernanceService.rollback_model_version(db=db, version_id=version_id, user_id=current_user.id)

@router.post("/drift-check")
def trigger_drift_check(
    disease_slug: str = Query(..., description="Disease identifier slug"),
    limit: int = Query(200, ge=10, le=1000),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist"]))
) -> Dict[str, Any]:
    """Evaluates KS-test and PSI feature drift between baseline training distribution and recorded inputs."""
    return GovernanceService.run_drift_check(db=db, disease_slug=disease_slug, limit_inferences=limit)
