"""
MedPredict AI — User Account & Profile Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.user import UserRead, UserUpdate
from backend.app.schemas.role import UserRoleAssign
from backend.app.services.user_service import UserService
from backend.app.security.deps import (
    get_current_active_user,
    require_roles
)
from backend.app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserRead, summary="Get Current User Profile")
def get_current_user_profile(current_user: User = Depends(get_current_active_user)):
    """Returns the authenticated user's profile and roles."""
    return current_user

@router.put("/me", response_model=UserRead, summary="Update Profile")
def update_current_user_profile(
    update_data: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Updates profile details for the authenticated user."""
    return UserService.update_profile(db, current_user, update_data)

@router.get(
    "/",
    response_model=List[UserRead],
    summary="List Users (Admin & Auditor Only)",
    dependencies=[Depends(require_roles("ADMIN", "AUDITOR"))]
)
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    role: Optional[str] = Query(None, description="Filter by role name"),
    db: Session = Depends(get_db)
):
    """Lists registered users with pagination and role filtering."""
    return UserService.list_users(db, skip=skip, limit=limit, role=role)

@router.post(
    "/{user_id}/roles",
    response_model=UserRead,
    summary="Assign User Roles (Admin Only)",
    dependencies=[Depends(require_roles("ADMIN"))]
)
def assign_roles(
    user_id: str,
    payload: UserRoleAssign,
    current_admin: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Assigns designated roles to a target user."""
    return UserService.assign_roles(db, user_id=user_id, role_names=payload.role_names, admin_user_id=current_admin.id)
