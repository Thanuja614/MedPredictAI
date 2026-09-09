"""
MedPredict AI — Generated Report Registry Models
"""

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Report(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Catalog of generated clinical, ML model card, and data quality reports."""
    __tablename__ = "reports"

    title = Column(String(200), nullable=False)
    report_type = Column(String(50), nullable=False, index=True)  # prediction_summary, patient_risk, data_quality, model_card
    format = Column(String(10), nullable=False)  # pdf, csv, xlsx
    file_path = Column(String(500), nullable=False)
    generated_by_user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    generated_by = relationship("User")
