"""
MedPredict AI — Background Jobs Endpoints
"""

from typing import Dict, Any, List
from fastapi import APIRouter, Depends, Path as FPath, Query
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.security.deps import require_roles
from backend.app.services.job_service import JobService

router = APIRouter()

@router.get("")
def list_background_jobs(
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist"]))
) -> List[Dict[str, Any]]:
    """List recent background tasks (training runs, batch scoring, dataset profiling)."""
    return JobService.list_jobs(db, limit=limit)

@router.get("/{job_id}")
def get_job_status(
    job_id: str = FPath(..., description="Job identifier"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin", "data_scientist"]))
) -> Dict[str, Any]:
    """Get current status and progress percent of a background task."""
    job = JobService.get_job(db, job_id)
    return {
        "id": job.id,
        "job_type": job.job_type,
        "status": job.status,
        "progress_percent": job.progress_percent,
        "error_message": job.error_message,
        "started_at": job.started_at.isoformat() if job.started_at else None,
        "completed_at": job.completed_at.isoformat() if job.completed_at else None
    }
