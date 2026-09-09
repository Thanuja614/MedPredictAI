"""
MedPredict AI — Notification Endpoints
"""

from typing import Dict, Any, List
from fastapi import APIRouter, Depends, Path as FPath, Query
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.security.deps import get_current_active_user
from backend.app.services.notification_service import NotificationService

router = APIRouter()

@router.get("")
def list_notifications(
    unread_only: bool = Query(False),
    limit: int = Query(30, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[Dict[str, Any]]:
    """List recent and unread notifications for current authenticated user."""
    return NotificationService.get_user_notifications(
        db=db,
        user_id=current_user.id,
        unread_only=unread_only,
        limit=limit
    )

@router.put("/{notification_id}/read")
def mark_notification_read(
    notification_id: str = FPath(..., description="Notification ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Mark a notification as read."""
    return NotificationService.mark_read(
        db=db,
        notification_id=notification_id,
        user_id=current_user.id
    )

@router.post("/mark-all-read")
def mark_all_notifications_read(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Mark all unread notifications as read."""
    return NotificationService.mark_all_read(db=db, user_id=current_user.id)
