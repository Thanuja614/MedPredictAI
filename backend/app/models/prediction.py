"""
MedPredict AI — Prediction, Inputs & Explainability Models
"""

from sqlalchemy import Column, String, Boolean, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Prediction(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Inference execution record tracking model probability, risk classification and patient linkage."""
    __tablename__ = "predictions"

    patient_id = Column(String(36), ForeignKey("patients.id", ondelete="SET NULL"), nullable=True)
    assessment_id = Column(String(36), ForeignKey("assessments.id", ondelete="SET NULL"), nullable=True)
    model_version_id = Column(String(36), ForeignKey("model_versions.id", ondelete="RESTRICT"), nullable=False)
    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="RESTRICT"), nullable=False)
    probability = Column(Float, nullable=False)  # 0.0 to 1.0
    risk_level = Column(String(20), nullable=False)  # LOW, MODERATE, HIGH
    is_batch = Column(Boolean, default=False, nullable=False)

    # Relationships
    patient = relationship("Patient", back_populates="predictions")
    assessment = relationship("Assessment", back_populates="predictions")
    model_version = relationship("ModelVersion", back_populates="predictions")
    disease = relationship("Disease", back_populates="predictions")
    input_data = relationship("PredictionInput", back_populates="prediction", uselist=False, cascade="all, delete-orphan")
    explanation = relationship("Explanation", back_populates="prediction", uselist=False, cascade="all, delete-orphan")

class PredictionInput(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Full snapshot of the raw input features used to generate the prediction."""
    __tablename__ = "prediction_inputs"

    prediction_id = Column(String(36), ForeignKey("predictions.id", ondelete="CASCADE"), unique=True, nullable=False)
    input_features_json = Column(Text, nullable=False)

    # Relationships
    prediction = relationship("Prediction", back_populates="input_data")

class Explanation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Local and global explainability output (SHAP waterfall values)."""
    __tablename__ = "explanations"

    prediction_id = Column(String(36), ForeignKey("predictions.id", ondelete="CASCADE"), unique=True, nullable=False)
    method = Column(String(50), default="SHAP_TREE", nullable=False)
    feature_contributions_json = Column(Text, nullable=False)
    base_value = Column(Float, nullable=True)

    # Relationships
    prediction = relationship("Prediction", back_populates="explanation")
