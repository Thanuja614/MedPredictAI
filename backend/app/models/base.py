"""
MedPredict AI — Base Model & Shared Mixins
"""

import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from backend.app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class TimestampMixin:
    """Provides automatic UTC creation and update timestamps."""
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

class UUIDPrimaryKeyMixin:
    """Provides string-compatible UUID primary keys for PostgreSQL and SQLite."""
    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
