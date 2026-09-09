"""
MedPredict AI — Machine Learning Lifecycle & Model Registry Models
"""

from sqlalchemy import Column, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class MLModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Registered ML model entity associated with a disease domain."""
    __tablename__ = "models"

    name = Column(String(150), unique=True, nullable=False, index=True)
    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="CASCADE"), nullable=False)
    description = Column(Text, nullable=True)

    # Relationships
    disease = relationship("Disease", back_populates="models")
    versions = relationship("ModelVersion", back_populates="model", cascade="all, delete-orphan")

class Experiment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """ML experiment grouping multiple training runs for a disease."""
    __tablename__ = "experiments"

    name = Column(String(150), nullable=False)
    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="CASCADE"), nullable=False)
    created_by_user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    disease = relationship("Disease", back_populates="experiments")
    training_runs = relationship("TrainingRun", back_populates="experiment", cascade="all, delete-orphan")

class TrainingRun(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Individual model training run execution record."""
    __tablename__ = "training_runs"

    experiment_id = Column(String(36), ForeignKey("experiments.id", ondelete="CASCADE"), nullable=False)
    dataset_version_id = Column(String(36), ForeignKey("dataset_versions.id", ondelete="RESTRICT"), nullable=False)
    algorithm = Column(String(100), nullable=False)
    hyperparameters_json = Column(Text, nullable=True)
    metrics_json = Column(Text, nullable=True)  # accuracy, precision, recall, f1, roc_auc
    duration_seconds = Column(Float, nullable=True)
    status = Column(String(30), default="pending", nullable=False)  # pending, running, completed, failed

    # Relationships
    experiment = relationship("Experiment", back_populates="training_runs")
    dataset_version = relationship("DatasetVersion", back_populates="training_runs")
    model_version = relationship("ModelVersion", back_populates="training_run", uselist=False)

class ModelVersion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Serialized, reproducible model artifact version registered for inference."""
    __tablename__ = "model_versions"

    model_id = Column(String(36), ForeignKey("models.id", ondelete="CASCADE"), nullable=False)
    training_run_id = Column(String(36), ForeignKey("training_runs.id", ondelete="CASCADE"), unique=True, nullable=False)
    version_tag = Column(String(30), nullable=False)
    artifact_path = Column(String(500), nullable=False)
    artifact_hash_sha256 = Column(String(64), nullable=False, index=True)
    status = Column(String(30), default="staged", nullable=False)  # staged, active, archived
    metrics_summary_json = Column(Text, nullable=True)

    # Relationships
    model = relationship("MLModel", back_populates="versions")
    training_run = relationship("TrainingRun", back_populates="model_version")
    predictions = relationship("Prediction", back_populates="model_version")
