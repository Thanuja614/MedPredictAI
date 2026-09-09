"""
MedPredict AI — Role & Permission Schemas
"""

from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict

class PermissionRead(BaseModel):
    id: int
    name: str
    module: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class RoleRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    permissions: List[PermissionRead] = []

    model_config = ConfigDict(from_attributes=True)

class UserRoleAssign(BaseModel):
    role_names: List[str] = Field(..., description="List of role names to assign to the user")
