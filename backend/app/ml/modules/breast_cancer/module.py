"""
MedPredict AI — Breast Cancer Prediction Module (Phase 13)
Implements cellular morphometric descriptor processing, shape distortion indexing,
model training, risk prediction, and local explainability.
"""

from typing import Any, Dict, List
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler

from backend.app.ml.framework.base_preprocessor import BasePreprocessor
from backend.app.ml.framework.base_feature_engineer import BaseFeatureEngineer
from backend.app.ml.framework.base_module import BaseDiseaseModule

RAW_FEATURES = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean"
]

class BreastCancerPreprocessor(BasePreprocessor):
    """Encapsulates scaling and median imputation for cellular morphology features."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "BreastCancerPreprocessor":
        df_copy = df[self.feature_names].copy()
        self.medians = {col: float(df_copy[col].median(skipna=True)) for col in self.feature_names}
        df_imputed = df_copy.fillna(self.medians)
        self.scaler.fit(df_imputed)
        self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.check_fitted()
        df_copy = df[self.feature_names].copy().fillna(self.medians)
        scaled_array = self.scaler.transform(df_copy)
        return pd.DataFrame(scaled_array, columns=self.feature_names, index=df.index)

class BreastCancerFeatureEngineer(BaseFeatureEngineer):
    """
    Derives cellular morphological descriptors:
    - Shape Distortion Index: (perimeter_mean ** 2) / (area_mean + 1e-5)
    - Malignancy Nuclear Score: radius_mean * concavity_mean
    - Density Irregularity: texture_mean * compactness_mean
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["shape_distortion_index"] = (df_out["perimeter_mean"] ** 2) / (df_out["area_mean"] + 1e-5)
        df_out["malignancy_nuclear_score"] = df_out["radius_mean"] * df_out["concavity_mean"]
        df_out["density_irregularity"] = df_out["texture_mean"] * df_out["compactness_mean"]
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["shape_distortion_index", "malignancy_nuclear_score", "density_irregularity"]

class BreastCancerDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Breast Malignancy Risk."""

    def __init__(self):
        super().__init__(
            name="Breast Cancer",
            slug="breast_cancer",
            category="Oncology",
            description="Cellular morphological risk analysis for breast lesion malignancy.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "radius_mean", "data_type": "float", "min_value": 5.0, "max_value": 35.0, "unit": "mm", "is_required": True},
            {"name": "texture_mean", "data_type": "float", "min_value": 8.0, "max_value": 45.0, "unit": "score", "is_required": True},
            {"name": "perimeter_mean", "data_type": "float", "min_value": 40.0, "max_value": 200.0, "unit": "mm", "is_required": True},
            {"name": "area_mean", "data_type": "float", "min_value": 100.0, "max_value": 2600.0, "unit": "mm^2", "is_required": True},
            {"name": "smoothness_mean", "data_type": "float", "min_value": 0.05, "max_value": 0.20, "unit": "score", "is_required": True},
            {"name": "compactness_mean", "data_type": "float", "min_value": 0.01, "max_value": 0.35, "unit": "score", "is_required": True},
            {"name": "concavity_mean", "data_type": "float", "min_value": 0.0, "max_value": 0.45, "unit": "score", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return BreastCancerFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return BreastCancerPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        }
