"""
MedPredict AI — Dataset Management & Quality Models
"""

from sqlalchemy import Column, String, Boolean, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Dataset(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Clinical or demonstration dataset entity attached to a disease module."""
    __tablename__ = "datasets"

    name = Column(String(150), unique=True, nullable=False, index=True)
    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="CASCADE"), nullable=False)
    source_description = Column(Text, nullable=True)
    is_synthetic = Column(Boolean, default=True, nullable=False)

    # Relationships
    disease = relationship("Disease", back_populates="datasets")
    versions = relationship("DatasetVersion", back_populates="dataset", cascade="all, delete-orphan")

class DatasetVersion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Versioned snapshot of an ingested dataset with integrity checksum."""
    __tablename__ = "dataset_versions"

    dataset_id = Column(String(36), ForeignKey("datasets.id", ondelete="CASCADE"), nullable=False)
    version_tag = Column(String(30), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_format = Column(String(20), nullable=False)  # csv, parquet, xlsx
    row_count = Column(Integer, nullable=False)
    column_count = Column(Integer, nullable=False)
    checksum_sha256 = Column(String(64), nullable=False, index=True)
    uploaded_by_user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    dataset = relationship("Dataset", back_populates="versions")
    quality_report = relationship("DataQualityReport", back_populates="dataset_version", uselist=False, cascade="all, delete-orphan")
    training_runs = relationship("TrainingRun", back_populates="dataset_version")

class DataQualityReport(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Automated data profiling and quality metrics report."""
    __tablename__ = "data_quality_reports"

    dataset_version_id = Column(String(36), ForeignKey("dataset_versions.id", ondelete="CASCADE"), unique=True, nullable=False)
    quality_score = Column(Float, nullable=False)  # 0.0 to 100.0
    missing_cell_count = Column(Integer, default=0, nullable=False)
    duplicate_row_count = Column(Integer, default=0, nullable=False)
    metrics_json = Column(Text, nullable=False)   # Serialized detailed metrics

    # Relationships
    dataset_version = relationship("DatasetVersion", back_populates="quality_report")
