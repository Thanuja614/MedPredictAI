"""
MedPredict AI — Authentication Endpoints
Handles user registration, login, JWT issuance, token rotation, and password reset.
"""

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.user import (
    UserCreate,
    UserLogin,
    UserRead,
    PasswordResetRequest,
    PasswordResetConfirm
)
from backend.app.schemas.token import Token, RefreshTokenRequest
from backend.app.services.auth_service import AuthService
from backend.app.core.errors import DataValidationError
from backend.app.security.deps import get_current_user
from backend.app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Register New User")
def register_user(user_in: UserCreate, request: Request, db: Session = Depends(get_db)):
    """Registers a new user account with default role."""
    client_ip = request.client.host if request.client else None
    return AuthService.register_user(db, user_in, ip_address=client_ip)

@router.post("/login", response_model=Token, summary="Authenticate & Retrieve JWT")
async def login(request: Request, db: Session = Depends(get_db)):
    """Authenticates credentials (accepts JSON or application/x-www-form-urlencoded) and returns JWT tokens."""
    client_ip = request.client.host if request.client else None
    content_type = request.headers.get("content-type", "").lower()
    
    if "application/x-www-form-urlencoded" in content_type or "multipart/form-data" in content_type:
        form = await request.form()
        email = form.get("username") or form.get("email")
        password = form.get("password")
    else:
        try:
            body = await request.json()
            email = body.get("email") or body.get("username")
            password = body.get("password")
        except Exception:
            raise DataValidationError("Invalid JSON or form payload")

    if not email or not password:
        raise DataValidationError("Email and password are required")

    credentials = UserLogin(email=email, password=password)
    _, token = AuthService.authenticate_user(db, credentials, ip_address=client_ip)
    return token

@router.post("/refresh", response_model=Token, summary="Rotate Refresh Token")
def refresh_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    """Issues a new short-lived access token using a valid refresh token."""
    return AuthService.refresh_token(db, payload.refresh_token)

@router.post("/logout", summary="Logout Current Session")
def logout(current_user: User = Depends(get_current_user)):
    """Logs out current user session."""
    return {"success": True, "message": f"User {current_user.email} logged out successfully"}

@router.post("/password-reset/request", summary="Request Password Reset")
def request_password_reset(payload: PasswordResetRequest, db: Session = Depends(get_db)):
    """Generates a secure password reset token."""
    token = AuthService.request_password_reset(db, payload.email)
    return {
        "success": True,
        "message": "If an account exists, a reset token has been issued.",
        "reset_token": token
    }

@router.post("/password-reset/confirm", summary="Confirm Password Reset")
def confirm_password_reset(payload: PasswordResetConfirm, db: Session = Depends(get_db)):
    """Applies a new password using a verified reset token."""
    AuthService.reset_password(db, payload.token, payload.new_password)
    return {"success": True, "message": "Password has been successfully updated"}
