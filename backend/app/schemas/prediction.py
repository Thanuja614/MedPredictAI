"""
MedPredict AI — Prediction & Inference Schemas
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class PredictionRequest(BaseModel):
    disease_slug: str = Field(..., description="Target disease slug (e.g. 'diabetes', 'heart')")
    patient_id: Optional[str] = Field(None, description="Optional patient UUID")
    assessment_id: Optional[str] = Field(None, description="Optional clinical assessment UUID")
    features: Dict[str, Any] = Field(..., description="Dictionary of input feature values")

class FeatureContribution(BaseModel):
    feature: str
    value: float
    contribution: float
    direction: str

class ExplanationRead(BaseModel):
    method: str
    base_value: float
    contributions: List[FeatureContribution]
    summary: str
    disclaimer: str

class ThresholdConfig(BaseModel):
    moderate_cutoff: float
    high_cutoff: float

class PredictionResponse(BaseModel):
    prediction_id: str
    id: Optional[str] = None
    disease_name: str
    disease_slug: str
    probability: float
    risk_level: str  # LOW, MODERATE, HIGH
    confidence_score: Optional[float] = 0.95
    thresholds: ThresholdConfig
    explanation: ExplanationRead
    explanations: Optional[Dict[str, Any]] = None
    disclaimer: str
    created_at: datetime

class PredictionHistoryItem(BaseModel):
    id: str
    disease_id: str
    probability: float
    risk_level: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
