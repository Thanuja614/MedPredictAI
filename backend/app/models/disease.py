"""
MedPredict AI — Disease & Feature Catalog Models
"""

from sqlalchemy import Column, String, Boolean, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Disease(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Catalog of supported disease prediction modules."""
    __tablename__ = "diseases"

    name = Column(String(100), unique=True, nullable=False, index=True)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)

    # Relationships
    features = relationship("DiseaseFeature", back_populates="disease", cascade="all, delete-orphan")
    datasets = relationship("Dataset", back_populates="disease", cascade="all, delete-orphan")
    models = relationship("MLModel", back_populates="disease", cascade="all, delete-orphan")
    experiments = relationship("Experiment", back_populates="disease", cascade="all, delete-orphan")
    assessments = relationship("Assessment", back_populates="disease")
    predictions = relationship("Prediction", back_populates="disease")

class DiseaseFeature(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Specification of an input feature required for a disease prediction module."""
    __tablename__ = "disease_features"

    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    data_type = Column(String(30), nullable=False)  # numeric, categorical, boolean
    unit = Column(String(30), nullable=True)
    min_value = Column(Float, nullable=True)
    max_value = Column(Float, nullable=True)
    is_required = Column(Boolean, default=True, nullable=False)
    description = Column(Text, nullable=True)

    # Relationships
    disease = relationship("Disease", back_populates="features")
