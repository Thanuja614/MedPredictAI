"""
MedPredict AI — Thyroid Dysfunction Module (Phase 17)
Implements endocrine hormonal data processing, Free Thyroxine Index (FTI) engineering,
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
    "age",
    "sex",
    "on_thyroxine",
    "tsh",
    "t3",
    "tt4",
    "t4u"
]

class ThyroidPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for thyroid hormonal markers."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "ThyroidPreprocessor":
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

class ThyroidFeatureEngineer(BaseFeatureEngineer):
    """
    Derives clinical thyroid functional indicators:
    - Free Thyroxine Index (FTI): tt4 / (t4u + 1e-5)
    - TSH to T3 Feedback Ratio: tsh / (t3 + 1e-5)
    - Primary Hypothyroidism Indicator: tsh > 4.5 mIU/L
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["fti_proxy"] = df_out["tt4"] / (df_out["t4u"] + 1e-5)
        df_out["tsh_t3_ratio"] = df_out["tsh"] / (df_out["t3"] + 1e-5)
        df_out["primary_hypothyroid_flag"] = (df_out["tsh"] > 4.5).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["fti_proxy", "tsh_t3_ratio", "primary_hypothyroid_flag"]

class ThyroidDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Thyroid Dysfunction Risk."""

    def __init__(self):
        super().__init__(
            name="Thyroid Disease",
            slug="thyroid",
            category="Endocrine",
            description="Thyroid functional impairment (hypothyroidism / hyperthyroidism) screening.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "age", "data_type": "integer", "min_value": 10, "max_value": 100, "unit": "years", "is_required": True},
            {"name": "sex", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "code", "is_required": True},
            {"name": "on_thyroxine", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "tsh", "data_type": "float", "min_value": 0.01, "max_value": 50.0, "unit": "mIU/L", "is_required": True},
            {"name": "t3", "data_type": "float", "min_value": 0.1, "max_value": 10.0, "unit": "nmol/L", "is_required": True},
            {"name": "tt4", "data_type": "float", "min_value": 10.0, "max_value": 300.0, "unit": "nmol/L", "is_required": True},
            {"name": "t4u", "data_type": "float", "min_value": 0.2, "max_value": 2.5, "unit": "ratio", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return ThyroidFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return ThyroidPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42)
        }
