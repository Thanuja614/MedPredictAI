"""
MedPredict AI — Authentication & RBAC Security Dependencies
Extracts JWT credentials and enforces role and permission policies.
"""

from typing import List, Callable
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.core.database import get_db
from backend.app.core.security import decode_token
from backend.app.core.errors import AuthenticationError, AuthorizationError
from backend.app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    auto_error=False
)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Validates bearer access token and retrieves the authenticated user."""
    if not token:
        raise AuthenticationError("Authorization header with Bearer token is required")

    payload = decode_token(token)
    if not payload:
        raise AuthenticationError("Invalid or expired authentication token")

    user_id = payload.get("sub")
    if not user_id:
        raise AuthenticationError("Token payload missing user identifier")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise AuthenticationError("User associated with token not found")

    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Verifies that the current user account is active."""
    if not current_user.is_active:
        raise AuthorizationError("Inactive user account")
    return current_user

def require_roles(*role_names: str) -> Callable:
    """
    Role-Based Access Control dependency factory.
    Enforces that current user holds at least one of the specified roles.
    """
    target_roles = {r.upper() for r in role_names}

    def role_checker(current_user: User = Depends(get_current_active_user)) -> User:
        user_roles = {r.name.upper() for r in current_user.roles}
        if not user_roles.intersection(target_roles):
            allowed = ", ".join(target_roles)
            raise AuthorizationError(f"Access denied. Requires one of roles: [{allowed}]")
        return current_user

    return role_checker

def require_permissions(*permission_names: str) -> Callable:
    """
    Fine-grained permission dependency factory.
    Enforces that current user holds all specified operational permissions.
    """
    required_perms = set(permission_names)

    def permission_checker(current_user: User = Depends(get_current_active_user)) -> User:
        user_perms = set()
        for r in current_user.roles:
            for p in r.permissions:
                user_perms.add(p.name)
        if not required_perms.issubset(user_perms):
            missing = ", ".join(required_perms - user_perms)
            raise AuthorizationError(f"Access denied. Missing required permissions: [{missing}]")
        return current_user

    return permission_checker
