"""
MedPredict AI — Local Model Registry & Lifecycle Engine (Phase 25)
Stores model artifacts, metadata, and SHA-256 hashes for reproducible inference.
"""

import os
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Optional
import pandas as pd
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.ml.modules import get_disease_module
from backend.app.models.disease import Disease
from backend.app.models.model import MLModel, ModelVersion, TrainingRun, Experiment

# Locate project root (5 levels up from backend/app/ml/registry/registry.py)
ROOT_DIR = Path(__file__).resolve().parents[4]
DATASETS_DIR = ROOT_DIR / "data" / "datasets"
MODELS_DIR = ROOT_DIR / "models" / "artifacts"

class ModelRegistry:
    """
    Manages active trained model instances for inference, artifact hashing,
    and automatic training on first launch from validated demonstration datasets.
    """

    _loaded_modules: Dict[str, Any] = {}

    @classmethod
    def get_active_module(cls, disease_slug: str, db: Optional[Session] = None) -> Any:
        """
        Retrieves the active trained module for a disease.
        If not yet in memory or on disk, trains baseline model from local dataset and caches it.
        """
        slug = disease_slug.lower().strip()
        if slug in cls._loaded_modules:
            return cls._loaded_modules[slug]

        module = get_disease_module(slug)
        artifact_dir = MODELS_DIR / slug / "v1.0.0"
        artifact_path = artifact_dir / f"{slug}_model_v1.0.0.joblib"

        # Check if serialized artifact exists on disk
        if artifact_path.exists():
            success = module.load_artifact(str(artifact_path))
            if success:
                cls._loaded_modules[slug] = module
                return module

        # Train from local demo dataset
        csv_path = DATASETS_DIR / slug / f"{slug}.csv"
        if not csv_path.exists():
            raise FileNotFoundError(f"No demonstration dataset found for '{slug}' at {csv_path}")

        df = pd.read_csv(csv_path)
        train_len = int(0.8 * len(df))
        df_train = df.iloc[:train_len]
        df_test = df.iloc[train_len:]

        # Fit module
        module.train_and_evaluate(df_train, df_test)

        # Save to disk
        saved_file = module.save_artifact(str(artifact_dir))

        # Compute SHA-256 checksum
        with open(saved_file, "rb") as f:
            art_bytes = f.read()
        sha256_hash = hashlib.sha256(art_bytes).hexdigest()

        # If database session is available, register in DB tables
        if db:
            disease = db.query(Disease).filter(Disease.slug == slug).first()
            if disease:
                model_rec = db.query(MLModel).filter(MLModel.disease_id == disease.id).first()
                if not model_rec:
                    model_rec = MLModel(name=f"{disease.name} Risk Estimator", disease_id=disease.id)
                    db.add(model_rec)
                    db.flush()

                exp = Experiment(name=f"{disease.name} Baseline Sweep", disease_id=disease.id)
                db.add(exp)
                db.flush()

                from backend.app.models.dataset import DatasetVersion
                ds_ver = db.query(DatasetVersion).first()
                if ds_ver:
                    run = TrainingRun(
                        experiment_id=exp.id,
                        dataset_version_id=ds_ver.id,
                        algorithm="random_forest",
                        metrics_json=json.dumps(module.evaluation_metrics),
                        status="completed"
                    )
                    db.add(run)
                    db.flush()

                    mv = ModelVersion(
                        model_id=model_rec.id,
                        training_run_id=run.id,
                        version_tag="1.0.0",
                        artifact_path=str(saved_file),
                        artifact_hash_sha256=sha256_hash,
                        status="active",
                        metrics_summary_json=json.dumps(module.evaluation_metrics)
                    )
                    db.add(mv)
                    db.commit()

        cls._loaded_modules[slug] = module
        return module
