"""
MedPredict AI — Authentication Business Logic Service
Coordinates registration, credential verification, token lifecycle and password recovery.
"""

from datetime import timedelta, datetime, timezone
from typing import Tuple, Optional
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.core.security import get_password_hash, verify_password, create_access_token, decode_token
from backend.app.core.errors import AuthenticationError, DataValidationError, EntityNotFoundError
from backend.app.models.user import User, Role
from backend.app.models.patient import Patient, MedicalProfile
from backend.app.models.audit import AuditLog
from backend.app.schemas.user import UserCreate, UserLogin
from backend.app.schemas.token import Token

class AuthService:

    @staticmethod
    def register_user(db: Session, user_in: UserCreate, ip_address: Optional[str] = None) -> User:
        """Registers a new user account with default PATIENT role if unspecified."""
        # Check email uniqueness
        existing = db.query(User).filter(User.email == user_in.email.lower()).first()
        if existing:
            raise DataValidationError(f"User with email '{user_in.email}' already exists")

        # Hash password securely with bcrypt
        hashed_pw = get_password_hash(user_in.password)

        new_user = User(
            email=user_in.email.lower(),
            hashed_password=hashed_pw,
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            is_active=True,
            is_verified=False
        )

        # Resolve role
        target_role_name = (user_in.role or "PATIENT").upper()
        role = db.query(Role).filter(Role.name == target_role_name).first()
        if not role:
            # Fallback create role if running on clean db
            role = Role(name=target_role_name, description=f"{target_role_name} role")
            db.add(role)
            db.flush()

        new_user.roles.append(role)
        db.add(new_user)
        db.flush()

        # If role is PATIENT, automatically create an initial Patient and MedicalProfile record
        if target_role_name == "PATIENT":
            patient = Patient(
                user_id=new_user.id,
                date_of_birth=datetime(1990, 1, 1).date(),
                gender="Not Specified"
            )
            db.add(patient)
            db.flush()
            profile = MedicalProfile(
                patient_id=patient.id,
                allergies="None documented",
                chronic_conditions="None documented"
            )
            db.add(profile)

        # Record audit log
        audit = AuditLog(
            user_id=new_user.id,
            action="USER_REGISTRATION",
            entity_type="users",
            entity_id=new_user.id,
            ip_address=ip_address,
            details_json=f'{{"role": "{target_role_name}"}}'
        )
        db.add(audit)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate_user(db: Session, credentials: UserLogin, ip_address: Optional[str] = None) -> Tuple[User, Token]:
        """Authenticates user credentials and issues access + refresh tokens."""
        user = db.query(User).filter(User.email == credentials.email.lower()).first()
        if not user or not verify_password(credentials.password, user.hashed_password):
            raise AuthenticationError("Invalid email or password")

        if not user.is_active:
            raise AuthenticationError("Account has been disabled")

        # Determine primary role for JWT claim
        primary_role = user.roles[0].name if user.roles else "PATIENT"

        # Generate tokens
        access_token = create_access_token(
            subject=user.id,
            extra_claims={"role": primary_role, "email": user.email}
        )

        # Generate long-lived refresh token
        refresh_delta = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = create_access_token(
            subject=user.id,
            expires_delta=refresh_delta,
            extra_claims={"type": "refresh", "role": primary_role}
        )

        # Audit login
        audit = AuditLog(
            user_id=user.id,
            action="USER_LOGIN_SUCCESS",
            entity_type="users",
            entity_id=user.id,
            ip_address=ip_address
        )
        db.add(audit)
        db.commit()

        token_response = Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
        return user, token_response

    @staticmethod
    def refresh_token(db: Session, refresh_token_str: str) -> Token:
        """Validates a refresh token and issues a fresh access token."""
        payload = decode_token(refresh_token_str)
        if not payload or payload.get("type") != "refresh":
            raise AuthenticationError("Invalid or expired refresh token")

        user_id = payload.get("sub")
        user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
        if not user:
            raise AuthenticationError("User associated with refresh token not found or inactive")

        primary_role = user.roles[0].name if user.roles else "PATIENT"
        new_access_token = create_access_token(
            subject=user.id,
            extra_claims={"role": primary_role, "email": user.email}
        )

        return Token(
            access_token=new_access_token,
            refresh_token=refresh_token_str,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )

    @staticmethod
    def request_password_reset(db: Session, email: str) -> str:
        """Issues a short-lived password reset token."""
        user = db.query(User).filter(User.email == email.lower()).first()
        if not user:
            # Prevent email enumeration by returning a valid-looking status
            return "If an account exists, a reset token has been generated."

        reset_token = create_access_token(
            subject=user.id,
            expires_delta=timedelta(minutes=15),
            extra_claims={"type": "reset_password"}
        )
        return reset_token

    @staticmethod
    def reset_password(db: Session, token: str, new_password: str) -> bool:
        """Validates reset token and sets new password hash."""
        payload = decode_token(token)
        if not payload or payload.get("type") != "reset_password":
            raise AuthenticationError("Invalid or expired password reset token")

        user_id = payload.get("sub")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise EntityNotFoundError("User not found")

        user.hashed_password = get_password_hash(new_password)
        db.commit()
        return True
