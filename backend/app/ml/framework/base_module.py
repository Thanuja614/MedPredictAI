"""
MedPredict AI — Standard Disease Module Base Class
Every disease module implements this standard interface across the platform.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import os
import json
import joblib
import pandas as pd

from backend.app.ml.framework.base_preprocessor import BasePreprocessor
from backend.app.ml.framework.base_feature_engineer import BaseFeatureEngineer
from backend.app.ml.framework.base_evaluator import ModelEvaluator
from backend.app.ml.framework.base_predictor import BasePredictor
from backend.app.ml.framework.base_explainer import BaseExplainer

class BaseDiseaseModule(ABC):
    """
    Standardized Disease Module contract.
    Guarantees consistent preprocessing, feature engineering, model candidates,
    evaluation, inference, explainability, and artifact serialization.
    """

    def __init__(
        self,
        name: str,
        slug: str,
        category: str,
        description: str,
        target_column: str,
        raw_features: List[str],
        version: str = "1.0.0"
    ):
        self.name = name
        self.slug = slug
        self.category = category
        self.description = description
        self.target_column = target_column
        self.raw_features = raw_features
        self.version = version

        self.preprocessor: Optional[BasePreprocessor] = None
        self.feature_engineer: Optional[BaseFeatureEngineer] = None
        self.active_model: Any = None
        self.predictor: Optional[BasePredictor] = None
        self.explainer: Optional[BaseExplainer] = None
        self.evaluation_metrics: Dict[str, Any] = {}

    @abstractmethod
    def get_feature_schema(self) -> List[Dict[str, Any]]:
        """Returns input feature definitions, types, units, and validation bounds."""
        pass

    @abstractmethod
    def build_preprocessor(self) -> BasePreprocessor:
        """Constructs disease-specific preprocessor pipeline."""
        pass

    @abstractmethod
    def build_feature_engineer(self) -> BaseFeatureEngineer:
        """Constructs disease-specific clinical feature engineering logic."""
        pass

    @abstractmethod
    def get_candidate_models(self) -> Dict[str, Any]:
        """Returns dictionary of ML model candidate estimators suited for this disease."""
        pass

    def train_and_evaluate(
        self,
        df_train: pd.DataFrame,
        df_test: pd.DataFrame,
        algorithm_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executes end-to-end training, hyperparameter fit, and test evaluation.
        Prevents data leakage by fitting preprocessor strictly on df_train.
        """
        self.preprocessor = self.build_preprocessor()
        self.feature_engineer = self.build_feature_engineer()

        # 1. Feature Engineering
        train_eng = self.feature_engineer.engineer_features(df_train)
        test_eng = self.feature_engineer.engineer_features(df_test)

        all_features = self.raw_features + self.feature_engineer.get_engineered_feature_names()

        # 2. Extract X and y
        X_train = train_eng[all_features]
        y_train = train_eng[self.target_column].values

        X_test = test_eng[all_features]
        y_test = test_eng[self.target_column].values

        # 3. Fit Preprocessor strictly on training data
        X_train_proc = self.preprocessor.fit_transform(X_train)
        X_test_proc = self.preprocessor.transform(X_test)

        # 4. Select and Fit Model Candidate
        candidates = self.get_candidate_models()
        algo = algorithm_name if algorithm_name in candidates else list(candidates.keys())[0]
        model = candidates[algo]
        model.fit(X_train_proc, y_train)

        self.active_model = model

        # 5. Evaluate on Holdout Test Data
        y_pred = model.predict(X_test_proc)
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test_proc)[:, 1]
        else:
            y_prob = y_pred

        metrics = ModelEvaluator.evaluate(y_test, y_pred, y_prob)
        metrics["algorithm"] = algo
        metrics["feature_count"] = len(all_features)
        self.evaluation_metrics = metrics

        # 6. Initialize Predictor and Explainer
        self.predictor = BasePredictor(model, self.preprocessor, all_features)
        self.explainer = BaseExplainer(model, all_features)

        return metrics

    def predict(self, input_features: Dict[str, Any]) -> Dict[str, Any]:
        """Runs inference and generates risk assessment and SHAP explanation."""
        if not self.predictor:
            raise ValueError(f"Module '{self.name}' has no active model trained yet.")

        # Engineer input features if necessary
        df_single = pd.DataFrame([input_features])
        if self.feature_engineer:
            df_single = self.feature_engineer.engineer_features(df_single)

        all_features = self.raw_features + (self.feature_engineer.get_engineered_feature_names() if self.feature_engineer else [])
        row_dict = df_single[all_features].iloc[0].to_dict()

        # Risk prediction
        pred_result = self.predictor.predict_risk(row_dict)

        # Explanation
        explanation_result = self.explainer.explain_instance(df_single[all_features])

        return {
            "disease": self.name,
            "slug": self.slug,
            "version": self.version,
            "prediction": pred_result,
            "explanation": explanation_result
        }

    def save_artifact(self, output_dir: str) -> str:
        """Serializes model, preprocessor, metadata, and evaluation metrics."""
        os.makedirs(output_dir, exist_ok=True)
        artifact_file = os.path.join(output_dir, f"{self.slug}_model_v{self.version}.joblib")
        metadata_file = os.path.join(output_dir, "metadata.json")
        metrics_file = os.path.join(output_dir, "metrics.json")

        bundle = {
            "model": self.active_model,
            "preprocessor": self.preprocessor,
            "feature_engineer": self.feature_engineer,
            "raw_features": self.raw_features,
            "version": self.version,
            "slug": self.slug
        }
        joblib.dump(bundle, artifact_file)

        with open(metadata_file, "w") as f:
            json.dump({
                "disease": self.name,
                "slug": self.slug,
                "version": self.version,
                "category": self.category,
                "target_column": self.target_column,
                "features": self.raw_features
            }, f, indent=2)

        with open(metrics_file, "w") as f:
            json.dump(self.evaluation_metrics, f, indent=2)

        return artifact_file

    def load_artifact(self, artifact_file: str) -> bool:
        """Loads serialized model bundle into memory."""
        if not os.path.exists(artifact_file):
            return False
        bundle = joblib.load(artifact_file)
        self.active_model = bundle["model"]
        self.preprocessor = bundle["preprocessor"]
        self.feature_engineer = bundle["feature_engineer"]
        all_features = self.raw_features + (self.feature_engineer.get_engineered_feature_names() if self.feature_engineer else [])
        self.predictor = BasePredictor(self.active_model, self.preprocessor, all_features)
        self.explainer = BaseExplainer(self.active_model, all_features)
        return True
