"""
MedPredict AI — User Account & Profile Schemas
"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from backend.app.schemas.role import RoleRead

class UserBase(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128, description="Minimum 8 characters")
    role: Optional[str] = Field(default="PATIENT", description="Initial role assignment (defaults to PATIENT)")

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    is_active: Optional[bool] = None

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8, max_length=128)

class UserRead(UserBase):
    id: str
    is_active: bool
    is_verified: bool
    roles: List[RoleRead] = []
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
