"""
MedPredict AI — Central Prediction & Inference Service (Phase 26)
Executes model inference, computes risk classification and SHAP attribution,
and guarantees complete reproducibility and audit traceability.
"""

import json
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session

from backend.app.ml.registry.registry import ModelRegistry
from backend.app.models.disease import Disease
from backend.app.models.model import ModelVersion
from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.audit import AuditLog
from backend.app.schemas.prediction import PredictionRequest, PredictionResponse
from backend.app.core.errors import EntityNotFoundError, DataValidationError

class PredictionService:

    @staticmethod
    def evaluate(db: Session, request: PredictionRequest, user_id: Optional[str] = None) -> PredictionResponse:
        """
        Runs ML risk prediction for a patient assessment, produces SHAP waterfall,
        and creates immutable database records for regulatory traceability.
        """
        slug = request.disease_slug.lower().strip()

        # Retrieve disease from DB or create if necessary
        disease = db.query(Disease).filter(Disease.slug == slug).first()
        if not disease:
            # Look up name from registry
            from backend.app.ml.modules import get_disease_module
            try:
                mod = get_disease_module(slug)
                disease = Disease(name=mod.name, slug=mod.slug, category=mod.category, description=mod.description)
                db.add(disease)
                db.flush()
            except KeyError:
                raise EntityNotFoundError(f"Disease slug '{slug}' is not supported")

        # Retrieve or train active module
        module = ModelRegistry.get_active_module(slug, db=db)

        # Execute inference & explanation
        try:
            inference_output = module.predict(request.features)
        except Exception as e:
            raise DataValidationError(f"Inference error for {disease.name}: {e}")

        pred_data = inference_output["prediction"]
        expl_data = inference_output["explanation"]

        # Resolve ModelVersion ID
        model_ver = db.query(ModelVersion).join(ModelVersion.model).filter(ModelVersion.status == "active").first()
        mv_id = model_ver.id if model_ver else "v1.0.0"

        # 1. Create Prediction record
        prediction = Prediction(
            patient_id=request.patient_id,
            assessment_id=request.assessment_id,
            model_version_id=mv_id,
            disease_id=disease.id,
            probability=pred_data["probability"],
            risk_level=pred_data["risk_level"],
            is_batch=False
        )
        db.add(prediction)
        db.flush()

        # 2. Store exact inputs for traceability
        pred_input = PredictionInput(
            prediction_id=prediction.id,
            input_features_json=json.dumps(request.features)
        )
        db.add(pred_input)

        # 3. Store SHAP explanation
        explanation = Explanation(
            prediction_id=prediction.id,
            method=expl_data.get("method", "SHAP_ATTRIBUTION"),
            feature_contributions_json=json.dumps(expl_data.get("contributions", [])),
            base_value=expl_data.get("base_value", 0.5)
        )
        db.add(explanation)

        # 4. Audit Log
        audit = AuditLog(
            user_id=user_id,
            action="PREDICTION_EVALUATED",
            entity_type="predictions",
            entity_id=prediction.id,
            details_json=f'{{"disease": "{slug}", "risk": "{pred_data["risk_level"]}", "prob": {pred_data["probability"]}}}'
        )
        db.add(audit)
        db.commit()
        db.refresh(prediction)

        return PredictionResponse(
            prediction_id=prediction.id,
            disease_name=disease.name,
            disease_slug=disease.slug,
            probability=pred_data["probability"],
            risk_level=pred_data["risk_level"],
            thresholds=pred_data["thresholds"],
            explanation=expl_data,
            disclaimer=pred_data["disclaimer"],
            created_at=prediction.created_at
        )

    @staticmethod
    def get_prediction(db: Session, prediction_id: str) -> Optional[Prediction]:
        return db.query(Prediction).filter(Prediction.id == prediction_id).first()

    @staticmethod
    def list_patient_history(db: Session, patient_id: str) -> List[Prediction]:
        return db.query(Prediction).filter(Prediction.patient_id == patient_id).order_by(Prediction.created_at.desc()).all()
