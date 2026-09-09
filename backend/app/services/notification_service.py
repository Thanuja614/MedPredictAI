"""
MedPredict AI — In-App Alerts & Notification Service
"""

from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, desc, update

from backend.app.models.job import Notification
from backend.app.core.errors import ResourceNotFoundError

class NotificationService:
    @staticmethod
    def create_notification(
        db: Session,
        user_id: str,
        title: str,
        message: str,
        notif_type: str = "info"  # info, success, warning, alert
    ) -> Notification:
        """Dispatches an in-app alert notification to a user."""
        notif = Notification(
            user_id=user_id,
            title=title,
            message=message,
            type=notif_type,
            is_read=False
        )
        db.add(notif)
        db.commit()
        db.refresh(notif)
        return notif

    @staticmethod
    def get_user_notifications(
        db: Session,
        user_id: str,
        unread_only: bool = False,
        limit: int = 30
    ) -> List[Dict[str, Any]]:
        query = select(Notification).where(Notification.user_id == user_id)
        if unread_only:
            query = query.where(Notification.is_read == False)
        query = query.order_by(desc(Notification.created_at)).limit(limit)

        notifs = db.execute(query).scalars().all()
        return [
            {
                "id": n.id,
                "title": n.title,
                "message": n.message,
                "type": n.type,
                "is_read": n.is_read,
                "created_at": n.created_at.isoformat() if n.created_at else None
            }
            for n in notifs
        ]

    @staticmethod
    def mark_read(db: Session, notification_id: str, user_id: str) -> Dict[str, Any]:
        notif = db.execute(
            select(Notification).where(Notification.id == notification_id, Notification.user_id == user_id)
        ).scalar_one_or_none()

        if not notif:
            raise ResourceNotFoundError("Notification", notification_id)

        notif.is_read = True
        db.commit()
        return {"id": notif.id, "is_read": True}

    @staticmethod
    def mark_all_read(db: Session, user_id: str) -> Dict[str, Any]:
        db.execute(
            update(Notification)
            .where(Notification.user_id == user_id, Notification.is_read == False)
            .values(is_read=True)
        )
        db.commit()
        return {"status": "success", "message": "All notifications marked as read"}
