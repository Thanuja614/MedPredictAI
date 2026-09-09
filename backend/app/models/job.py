"""
MedPredict AI — Background Jobs & In-App Notification Models
"""

from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Job(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Background asynchronous task execution state."""
    __tablename__ = "jobs"

    job_type = Column(String(50), nullable=False, index=True)  # model_training, batch_prediction, profiling, report_gen
    status = Column(String(30), default="pending", nullable=False, index=True)  # pending, running, succeeded, failed
    progress_percent = Column(Integer, default=0, nullable=False)
    error_message = Column(Text, nullable=True)
    payload_json = Column(Text, nullable=True)
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

class Notification(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """In-app alert notification delivered to users."""
    __tablename__ = "notifications"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    type = Column(String(50), default="info", nullable=False)  # info, success, warning, alert

    # Relationships
    user = relationship("User", back_populates="notifications")
