"""
MedPredict AI — Patient, Clinical History & Assessment Schemas
"""

from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict

class MedicalProfileBase(BaseModel):
    allergies: Optional[str] = Field(None, description="Allergies (medications, foods, environmental)")
    chronic_conditions: Optional[str] = Field(None, description="Documented chronic conditions")
    family_history: Optional[str] = Field(None, description="Family medical history")
    lifestyle_notes: Optional[str] = Field(None, description="Smoking, alcohol, exercise, dietary habits")

class MedicalProfileUpdate(MedicalProfileBase):
    pass

class MedicalProfileRead(MedicalProfileBase):
    id: str
    patient_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PatientBase(BaseModel):
    date_of_birth: date
    gender: str = Field(..., max_length=20)
    blood_group: Optional[str] = Field(None, max_length=5)
    emergency_contact: Optional[str] = Field(None, max_length=100)

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    emergency_contact: Optional[str] = None

class PatientRead(PatientBase):
    id: str
    user_id: str
    medical_profile: Optional[MedicalProfileRead] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AssessmentCreate(BaseModel):
    disease_id: str
    notes: Optional[str] = None

class AssessmentRead(BaseModel):
    id: str
    patient_id: str
    created_by_user_id: Optional[str] = None
    disease_id: str
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
