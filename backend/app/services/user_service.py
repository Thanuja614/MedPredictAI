"""
MedPredict AI — User Management & Governance Service
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.models.user import User, Role
from backend.app.models.audit import AuditLog
from backend.app.schemas.user import UserUpdate
from backend.app.core.errors import EntityNotFoundError, DataValidationError

class UserService:

    @staticmethod
    def get_by_id(db: Session, user_id: str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email.lower()).first()

    @staticmethod
    def list_users(db: Session, skip: int = 0, limit: int = 50, role: Optional[str] = None) -> List[User]:
        query = db.query(User)
        if role:
            query = query.join(User.roles).filter(Role.name == role.upper())
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_profile(db: Session, user: User, update_data: UserUpdate) -> User:
        if update_data.first_name is not None:
            user.first_name = update_data.first_name
        if update_data.last_name is not None:
            user.last_name = update_data.last_name
        if update_data.is_active is not None:
            user.is_active = update_data.is_active
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def assign_roles(db: Session, user_id: str, role_names: List[str], admin_user_id: str) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise EntityNotFoundError(f"User '{user_id}' not found")

        # Resolve roles
        new_roles = []
        for r_name in role_names:
            role = db.query(Role).filter(Role.name == r_name.upper()).first()
            if not role:
                raise DataValidationError(f"Role '{r_name}' does not exist")
            new_roles.append(role)

        user.roles = new_roles
        
        # Audit role assignment
        audit = AuditLog(
            user_id=admin_user_id,
            action="ROLES_UPDATED",
            entity_type="users",
            entity_id=user.id,
            details_json=f'{{"assigned_roles": {role_names}}}'
        )
        db.add(audit)
        db.commit()
        db.refresh(user)
        return user
