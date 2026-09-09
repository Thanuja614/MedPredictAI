"""
MedPredict AI — Structured Audit Trail & Security Event Models
"""

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class AuditLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Immutable audit entry for user and administrative transactions."""
    __tablename__ = "audit_logs"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    action = Column(String(100), nullable=False, index=True)
    entity_type = Column(String(100), nullable=False, index=True)
    entity_id = Column(String(100), nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(255), nullable=True)
    details_json = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", back_populates="audit_logs")

class SystemEvent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Platform system operational logs and component status changes."""
    __tablename__ = "system_events"

    event_type = Column(String(100), nullable=False, index=True)
    severity = Column(String(20), default="info", nullable=False)  # info, warning, error, critical
    message = Column(Text, nullable=False)
    metadata_json = Column(Text, nullable=True)

class SecurityEvent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Security incidents: brute force attempts, unauthorized access, suspicious payloads."""
    __tablename__ = "security_events"

    event_type = Column(String(100), nullable=False, index=True)
    ip_address = Column(String(50), nullable=True, index=True)
    user_identifier = Column(String(255), nullable=True)
    severity = Column(String(20), default="warning", nullable=False)
