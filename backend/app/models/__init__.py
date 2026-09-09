"""
MedPredict AI — Master Model Registry Package
Exports all SQLAlchemy ORM models for table discovery and migrations.
"""

from backend.app.core.database import Base
from backend.app.models.base import TimestampMixin, UUIDPrimaryKeyMixin
from backend.app.models.user import User, Role, Permission, UserRole, RolePermission
from backend.app.models.patient import Patient, Doctor, MedicalProfile, Assessment
from backend.app.models.disease import Disease, DiseaseFeature
from backend.app.models.dataset import Dataset, DatasetVersion, DataQualityReport
from backend.app.models.model import MLModel, Experiment, TrainingRun, ModelVersion
from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.audit import AuditLog, SystemEvent, SecurityEvent
from backend.app.models.job import Job, Notification
from backend.app.models.report import Report
from backend.app.models.setting import SystemSetting

__all__ = [
    "Base",
    "TimestampMixin",
    "UUIDPrimaryKeyMixin",
    "User",
    "Role",
    "Permission",
    "UserRole",
    "RolePermission",
    "Patient",
    "Doctor",
    "MedicalProfile",
    "Assessment",
    "Disease",
    "DiseaseFeature",
    "Dataset",
    "DatasetVersion",
    "DataQualityReport",
    "MLModel",
    "Experiment",
    "TrainingRun",
    "ModelVersion",
    "Prediction",
    "PredictionInput",
    "Explanation",
    "AuditLog",
    "SystemEvent",
    "SecurityEvent",
    "Job",
    "Notification",
    "Report",
    "SystemSetting"
]
