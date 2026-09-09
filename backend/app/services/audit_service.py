"""
MedPredict AI — Audit Trail & Security Compliance Service
Provides tamper-evident record keeping for clinical and administrative actions.
"""

from typing import Dict, Any, List, Optional
import io
import csv
import json
from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from backend.app.models.audit import AuditLog

class AuditService:
    @staticmethod
    def log(
        db: Session,
        action: str,
        entity_type: str,
        entity_id: Optional[str] = None,
        user_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ) -> AuditLog:
        """Records an immutable audit event."""
        log_entry = AuditLog(
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
            details_json=json.dumps(details) if details else None
        )
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)
        return log_entry

    @staticmethod
    def query_logs(
        db: Session,
        action: Optional[str] = None,
        entity_type: Optional[str] = None,
        user_id: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Queries audit events with filtering and pagination."""
        query = select(AuditLog)
        if action:
            query = query.where(AuditLog.action == action)
        if entity_type:
            query = query.where(AuditLog.entity_type == entity_type)
        if user_id:
            query = query.where(AuditLog.user_id == user_id)

        query = query.order_by(desc(AuditLog.created_at)).offset(offset).limit(limit)
        logs = db.execute(query).scalars().all()

        return {
            "total_returned": len(logs),
            "logs": [
                {
                    "id": l.id,
                    "action": l.action,
                    "entity_type": l.entity_type,
                    "entity_id": l.entity_id,
                    "user_id": l.user_id,
                    "user_email": l.user.email if l.user else None,
                    "ip_address": l.ip_address,
                    "user_agent": l.user_agent,
                    "details": json.loads(l.details_json) if l.details_json else {},
                    "created_at": l.created_at.isoformat() if l.created_at else None
                }
                for l in logs
            ]
        }

    @staticmethod
    def export_csv(db: Session, limit: int = 1000) -> str:
        """Exports audit entries as CSV string for external compliance analysis."""
        logs = db.execute(
            select(AuditLog).order_by(desc(AuditLog.created_at)).limit(limit)
        ).scalars().all()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "created_at", "action", "entity_type", "entity_id", "user_id", "ip_address", "details"])

        for l in logs:
            writer.writerow([
                l.id,
                l.created_at.isoformat() if l.created_at else "",
                l.action,
                l.entity_type,
                l.entity_id or "",
                l.user_id or "",
                l.ip_address or "",
                l.details_json or ""
            ])

        return output.getvalue()
