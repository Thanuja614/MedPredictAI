"""
MedPredict AI — ML Framework Base Contract Test Suite
Verifies preprocessors, feature engineering, training, evaluation, inference, and serialization.
"""

import os
import tempfile
import numpy as np
import pandas as pd
from typing import Dict, List, Any
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from backend.app.ml.framework.base_preprocessor import BasePreprocessor
from backend.app.ml.framework.base_feature_engineer import BaseFeatureEngineer
from backend.app.ml.framework.base_module import BaseDiseaseModule
from backend.app.ml.framework.base_predictor import MEDICAL_SAFETY_DISCLAIMER
from backend.app.ml.framework.base_explainer import SHAP_CAUSATION_DISCLAIMER

class MockPreprocessor(BasePreprocessor):
    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names)
        self.scaler = StandardScaler()

    def fit(self, df: pd.DataFrame) -> "MockPreprocessor":
        self.scaler.fit(df[self.feature_names])
        self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.check_fitted()
        scaled = self.scaler.transform(df[self.feature_names])
        return pd.DataFrame(scaled, columns=self.feature_names)

class MockFeatureEngineer(BaseFeatureEngineer):
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()
        df_copy["feature_ratio"] = df_copy["feat_a"] / (df_copy["feat_b"] + 1e-5)
        return df_copy

    def get_engineered_feature_names(self) -> List[str]:
        return ["feature_ratio"]

class MockDiseaseModule(BaseDiseaseModule):
    def __init__(self):
        super().__init__(
            name="Mock Disease",
            slug="mock_disease",
            category="Testing",
            description="Mock disease module for architecture validation",
            target_column="outcome",
            raw_features=["feat_a", "feat_b"]
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "feat_a", "data_type": "numeric", "min_value": 0.0, "max_value": 100.0, "is_required": True},
            {"name": "feat_b", "data_type": "numeric", "min_value": 0.0, "max_value": 100.0, "is_required": True}
        ]

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return MockPreprocessor(all_features)

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return MockFeatureEngineer()

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(random_state=42)
        }

def test_ml_framework_end_to_end():
    # 1. Generate synthetic reproducible dataset
    np.random.seed(42)
    n_samples = 200
    feat_a = np.random.normal(50, 10, n_samples)
    feat_b = np.random.normal(25, 5, n_samples)
    outcome = (feat_a * 0.4 + feat_b * 0.8 + np.random.normal(0, 5, n_samples) > 40).astype(int)

    df = pd.DataFrame({"feat_a": feat_a, "feat_b": feat_b, "outcome": outcome})
    df_train = df.iloc[:150]
    df_test = df.iloc[150:]

    # 2. Instantiate and train disease module
    module = MockDiseaseModule()
    metrics = module.train_and_evaluate(df_train, df_test, algorithm_name="logistic_regression")

    assert "accuracy" in metrics
    assert "roc_auc" in metrics
    assert metrics["accuracy"] >= 0.5
    assert metrics["sample_count"] == 50

    # 3. Test inference & safety disclaimer
    single_input = {"feat_a": 65.0, "feat_b": 35.0}
    prediction = module.predict(single_input)

    assert prediction["disease"] == "Mock Disease"
    pred_res = prediction["prediction"]
    assert "probability" in pred_res
    assert 0.0 <= pred_res["probability"] <= 1.0
    assert pred_res["risk_level"] in ("LOW", "MODERATE", "HIGH")
    assert pred_res["disclaimer"] == MEDICAL_SAFETY_DISCLAIMER

    # 4. Test explainability & causation disclaimer
    explanation = prediction["explanation"]
    assert "contributions" in explanation
    assert len(explanation["contributions"]) > 0
    assert explanation["disclaimer"] == SHAP_CAUSATION_DISCLAIMER

    # 5. Test artifact persistence and reload
    with tempfile.TemporaryDirectory() as tmpdir:
        art_path = module.save_artifact(tmpdir)
        assert os.path.exists(art_path)

        reloaded_module = MockDiseaseModule()
        loaded = reloaded_module.load_artifact(art_path)
        assert loaded is True

        reloaded_pred = reloaded_module.predict(single_input)
        assert reloaded_pred["prediction"]["risk_level"] == pred_res["risk_level"]
