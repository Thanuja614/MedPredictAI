"""
MedPredict AI — Audit Trail Endpoints
"""

from typing import Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.security.deps import require_roles
from backend.app.services.audit_service import AuditService

router = APIRouter()

@router.get("/logs")
def query_audit_logs(
    action: Optional[str] = Query(None),
    entity_type: Optional[str] = Query(None),
    user_id: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin"]))
) -> Dict[str, Any]:
    """Query immutable audit events with filtering and pagination."""
    return AuditService.query_logs(
        db=db,
        action=action,
        entity_type=entity_type,
        user_id=user_id,
        limit=limit,
        offset=offset
    )

@router.get("/export")
def export_audit_logs_csv(
    limit: int = Query(1000, ge=1, le=5000),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["admin"]))
):
    """Exports audit logs as a downloadable CSV for HIPAA/GDPR compliance verification."""
    csv_content = AuditService.export_csv(db=db, limit=limit)
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=medpredict_audit_log.csv"}
    )
