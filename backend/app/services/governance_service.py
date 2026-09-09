"""
MedPredict AI — Model Governance, Lifecycle & Monitoring Service
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pathlib import Path
import json
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from backend.app.core.errors import ResourceNotFoundError, BusinessRuleViolationError
from backend.app.models.model import MLModel, ModelVersion, TrainingRun
from backend.app.models.prediction import Prediction, PredictionInput
from backend.app.models.disease import Disease
from backend.app.models.audit import AuditLog
from backend.app.ml.monitoring.drift_detector import DriftDetector

class GovernanceService:
    @staticmethod
    def list_models_governance(db: Session) -> List[Dict[str, Any]]:
        """Lists all registered models along with their versions and governance status."""
        models = db.execute(select(MLModel)).scalars().all()
        result = []
        for m in models:
            versions = db.execute(
                select(ModelVersion)
                .where(ModelVersion.model_id == m.id)
                .order_by(desc(ModelVersion.created_at))
            ).scalars().all()

            v_list = []
            for v in versions:
                metrics = {}
                if v.metrics_summary_json:
                    try:
                        metrics = json.loads(v.metrics_summary_json)
                    except Exception:
                        metrics = {}

                v_list.append({
                    "id": v.id,
                    "version_tag": v.version_tag,
                    "status": v.status,  # staged, active, archived, shadow
                    "artifact_hash_sha256": v.artifact_hash_sha256,
                    "metrics": metrics,
                    "created_at": v.created_at.isoformat() if v.created_at else None
                })

            result.append({
                "model_id": m.id,
                "name": m.name,
                "disease_id": m.disease_id,
                "disease_name": m.disease.name if m.disease else "Unknown",
                "versions": v_list
            })
        return result

    @staticmethod
    def promote_model_version(
        db: Session,
        version_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Promotes a model version to 'active' (champion) and demotes any existing
        active version of the same model to 'archived'.
        """
        target_version = db.execute(
            select(ModelVersion).where(ModelVersion.id == version_id)
        ).scalar_one_or_none()

        if not target_version:
            raise ResourceNotFoundError("ModelVersion", version_id)

        # Demote existing active versions of the same model
        current_active = db.execute(
            select(ModelVersion).where(
                ModelVersion.model_id == target_version.model_id,
                ModelVersion.status == "active",
                ModelVersion.id != target_version.id
            )
        ).scalars().all()

        for old in current_active:
            old.status = "archived"

        target_version.status = "active"

        # Log governance event
        audit = AuditLog(
            user_id=user_id,
            action="MODEL_PROMOTED",
            entity_type="ModelVersion",
            entity_id=target_version.id,
            details_json=json.dumps({
                "version_tag": target_version.version_tag,
                "model_id": target_version.model_id,
                "new_status": "active"
            })
        )
        db.add(audit)
        db.commit()
        db.refresh(target_version)

        return {
            "version_id": target_version.id,
            "version_tag": target_version.version_tag,
            "status": target_version.status,
            "message": f"Version {target_version.version_tag} promoted to ACTIVE champion."
        }

    @staticmethod
    def rollback_model_version(
        db: Session,
        version_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Rolls back to a specific target version, demoting the currently active version.
        """
        target_version = db.execute(
            select(ModelVersion).where(ModelVersion.id == version_id)
        ).scalar_one_or_none()

        if not target_version:
            raise ResourceNotFoundError("ModelVersion", version_id)

        current_active = db.execute(
            select(ModelVersion).where(
                ModelVersion.model_id == target_version.model_id,
                ModelVersion.status == "active"
            )
        ).scalars().all()

        for act in current_active:
            act.status = "archived"

        target_version.status = "active"

        audit = AuditLog(
            user_id=user_id,
            action="MODEL_ROLLBACK",
            entity_type="ModelVersion",
            entity_id=target_version.id,
            details_json=json.dumps({
                "version_tag": target_version.version_tag,
                "model_id": target_version.model_id,
                "new_status": "active"
            })
        )
        db.add(audit)
        db.commit()
        db.refresh(target_version)

        return {
            "version_id": target_version.id,
            "version_tag": target_version.version_tag,
            "status": target_version.status,
            "message": f"Rolled back to version {target_version.version_tag} as ACTIVE."
        }

    @staticmethod
    def run_drift_check(
        db: Session,
        disease_slug: str,
        limit_inferences: int = 200
    ) -> Dict[str, Any]:
        """
        Extracts reference training data and recent prediction inputs to run KS and PSI drift metrics.
        """
        disease = db.execute(
            select(Disease).where(Disease.slug == disease_slug)
        ).scalar_one_or_none()

        if not disease:
            raise ResourceNotFoundError("Disease", disease_slug)

        # Baseline training data
        ref_path = Path("data") / "datasets" / disease_slug / f"{disease_slug}.csv"
        if not ref_path.exists():
            raise BusinessRuleViolationError(f"Baseline dataset not found for disease '{disease_slug}'")

        ref_df = pd.read_csv(ref_path)

        # Fetch recent prediction inputs for this disease
        preds = db.execute(
            select(Prediction)
            .where(Prediction.disease_id == disease.id)
            .order_by(desc(Prediction.created_at))
            .limit(limit_inferences)
        ).scalars().all()

        current_records = []
        for p in preds:
            if p.input_data and p.input_data.input_features_json:
                try:
                    data = json.loads(p.input_data.input_features_json)
                    current_records.append(data)
                except Exception:
                    pass

        if len(current_records) < 5:
            return {
                "disease_slug": disease_slug,
                "status": "INSUFFICIENT_DATA",
                "message": f"Only {len(current_records)} inference inputs recorded. Need at least 5 for drift testing.",
                "overall_drift_detected": False
            }

        curr_df = pd.DataFrame(current_records)
        num_cols = [c for c in curr_df.columns if c in ref_df.columns and pd.api.types.is_numeric_dtype(ref_df[c])]

        drift_summary = DriftDetector.evaluate_feature_drift(
            reference_df=ref_df,
            current_df=curr_df,
            numerical_features=num_cols
        )

        return {
            "disease_slug": disease_slug,
            "sample_size_reference": len(ref_df),
            "sample_size_current": len(curr_df),
            "evaluated_features_count": len(num_cols),
            **drift_summary
        }
