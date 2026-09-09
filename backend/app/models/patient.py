"""
MedPredict AI — Clinical & Patient Profile Models
"""

from sqlalchemy import Column, String, Date, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from backend.app.core.database import Base
from backend.app.models.base import UUIDPrimaryKeyMixin, TimestampMixin

class Patient(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Clinical patient demographic and profile record."""
    __tablename__ = "patients"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(20), nullable=False)
    blood_group = Column(String(5), nullable=True)
    emergency_contact = Column(String(100), nullable=True)

    # Relationships
    user = relationship("User", back_populates="patient_profile")
    medical_profile = relationship("MedicalProfile", back_populates="patient", uselist=False, cascade="all, delete-orphan")
    assessments = relationship("Assessment", back_populates="patient", cascade="all, delete-orphan")
    predictions = relationship("Prediction", back_populates="patient")

class Doctor(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Clinical provider record with license and hospital affiliation."""
    __tablename__ = "doctors"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    license_number = Column(String(100), unique=True, nullable=False, index=True)
    specialization = Column(String(100), nullable=False)
    hospital_affiliation = Column(String(255), nullable=True)

    # Relationships
    user = relationship("User", back_populates="doctor_profile")

class MedicalProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Longitudinal clinical history, allergies, and chronic conditions."""
    __tablename__ = "medical_profiles"

    patient_id = Column(String(36), ForeignKey("patients.id", ondelete="CASCADE"), unique=True, nullable=False)
    allergies = Column(Text, nullable=True)            # JSON or comma-delimited string
    chronic_conditions = Column(Text, nullable=True)   # JSON or comma-delimited string
    family_history = Column(Text, nullable=True)       # JSON or description
    lifestyle_notes = Column(Text, nullable=True)

    # Relationships
    patient = relationship("Patient", back_populates="medical_profile")

class Assessment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Clinical encounter or self-service disease assessment session."""
    __tablename__ = "assessments"

    patient_id = Column(String(36), ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)
    created_by_user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    disease_id = Column(String(36), ForeignKey("diseases.id", ondelete="RESTRICT"), nullable=False)
    notes = Column(Text, nullable=True)

    # Relationships
    patient = relationship("Patient", back_populates="assessments")
    disease = relationship("Disease", back_populates="assessments")
    predictions = relationship("Prediction", back_populates="assessment")
