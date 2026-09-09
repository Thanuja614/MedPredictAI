"""
MedPredict AI — Token & Authentication Schemas
"""

from typing import Optional
from pydantic import BaseModel, Field

class Token(BaseModel):
    """Authentication token response payload."""
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None
    expires_in: int

class TokenPayload(BaseModel):
    """Decoded JWT claims payload."""
    sub: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None
    exp: Optional[int] = None
    type: Optional[str] = None

class RefreshTokenRequest(BaseModel):
    """Request payload for rotating a refresh token."""
    refresh_token: str = Field(..., description="Valid non-expired refresh token")
