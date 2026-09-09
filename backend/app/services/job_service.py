"""
MedPredict AI — Background Jobs & Task Tracking Service
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
import json
from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from backend.app.core.errors import ResourceNotFoundError
from backend.app.models.job import Job

class JobService:
    @staticmethod
    def create_job(
        db: Session,
        job_type: str,
        payload: Optional[Dict[str, Any]] = None
    ) -> Job:
        """Enqueues a new background job."""
        job = Job(
            job_type=job_type,
            status="pending",
            progress_percent=0,
            payload_json=json.dumps(payload or {}),
            started_at=datetime.now(timezone.utc)
        )
        db.add(job)
        db.commit()
        db.refresh(job)
        return job

    @staticmethod
    def update_job_progress(
        db: Session,
        job_id: str,
        progress_percent: int,
        status: Optional[str] = None,
        error_message: Optional[str] = None
    ) -> Job:
        """Updates progress and status of a running job."""
        job = db.execute(select(Job).where(Job.id == job_id)).scalar_one_or_none()
        if not job:
            raise ResourceNotFoundError("Job", job_id)

        job.progress_percent = min(100, max(0, progress_percent))
        if status:
            job.status = status
            if status in ("succeeded", "failed"):
                job.completed_at = datetime.now(timezone.utc)
        if error_message:
            job.error_message = error_message

        db.commit()
        db.refresh(job)
        return job

    @staticmethod
    def get_job(db: Session, job_id: str) -> Job:
        job = db.execute(select(Job).where(Job.id == job_id)).scalar_one_or_none()
        if not job:
            raise ResourceNotFoundError("Job", job_id)
        return job

    @staticmethod
    def list_jobs(db: Session, limit: int = 50) -> List[Dict[str, Any]]:
        jobs = db.execute(select(Job).order_by(desc(Job.created_at)).limit(limit)).scalars().all()
        return [
            {
                "id": j.id,
                "job_type": j.job_type,
                "status": j.status,
                "progress_percent": j.progress_percent,
                "error_message": j.error_message,
                "started_at": j.started_at.isoformat() if j.started_at else None,
                "completed_at": j.completed_at.isoformat() if j.completed_at else None,
                "created_at": j.created_at.isoformat() if j.created_at else None
            }
            for j in jobs
        ]
