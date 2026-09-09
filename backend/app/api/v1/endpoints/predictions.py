"""
MedPredict AI — Prediction, Risk Classification & Explainability Endpoints
"""

import json
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
    PredictionHistoryItem
)
from backend.app.services.prediction_service import PredictionService
from backend.app.security.deps import (
    get_current_active_user,
    require_roles
)
from backend.app.core.errors import EntityNotFoundError, AuthorizationError
from backend.app.models.user import User

router = APIRouter(prefix="/predictions", tags=["Predictions & Inference"])

@router.post(
    "/evaluate",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Evaluate Disease Risk & SHAP Explanation"
)
def evaluate_prediction(
    request: PredictionRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Executes machine learning risk prediction for a selected disease module,
    computes local SHAP waterfall attribution, and attaches the mandatory medical safety disclaimer.
    """
    return PredictionService.evaluate(db, request, user_id=current_user.id)

@router.get(
    "/history",
    response_model=List[PredictionHistoryItem],
    summary="Get Patient Prediction History"
)
def get_prediction_history(
    patient_id: str = Query(..., description="Target patient UUID"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Retrieves longitudinal risk prediction history for trend analytics."""
    return PredictionService.list_patient_history(db, patient_id)

@router.get(
    "/{prediction_id}",
    summary="Get Prediction Details & Explanation"
)
def get_prediction_detail(
    prediction_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Retrieves full prediction breakdown, input features snapshot, and SHAP explanation."""
    pred = PredictionService.get_prediction(db, prediction_id)
    if not pred:
        raise EntityNotFoundError(f"Prediction '{prediction_id}' not found")

    inputs_dict = json.loads(pred.input_data.input_features_json) if pred.input_data else {}
    expl_dict = {}
    if pred.explanation:
        expl_dict = {
            "method": pred.explanation.method,
            "base_value": pred.explanation.base_value,
            "contributions": json.loads(pred.explanation.feature_contributions_json)
        }

    return {
        "id": pred.id,
        "disease_id": pred.disease_id,
        "probability": pred.probability,
        "risk_level": pred.risk_level,
        "inputs": inputs_dict,
        "explanation": expl_dict,
        "created_at": pred.created_at
    }
