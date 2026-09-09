"""
MedPredict AI — Parkinson's Disease Phonation Module (Phase 18)
Implements acoustic voice biomarker processing, vocal perturbation index engineering,
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
    "fo_hz",
    "fhi_hz",
    "flo_hz",
    "jitter_percent",
    "shimmer",
    "hnr",
    "rpde"
]

class ParkinsonsPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for acoustic phonation markers."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "ParkinsonsPreprocessor":
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

class ParkinsonsFeatureEngineer(BaseFeatureEngineer):
    """
    Derives vocal tremor & acoustic dysphonia indicators:
    - Fundamental Frequency Range: fhi_hz - flo_hz
    - Phonation Perturbation Index: (jitter_percent * 1000.0) * shimmer
    - Vocal Noise Fraction: 1.0 / (hnr + 1e-5)
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["vocal_frequency_range"] = df_out["fhi_hz"] - df_out["flo_hz"]
        df_out["phonation_perturbation_index"] = (df_out["jitter_percent"] * 1000.0) * df_out["shimmer"]
        df_out["vocal_noise_fraction"] = 1.0 / (df_out["hnr"] + 1e-5)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["vocal_frequency_range", "phonation_perturbation_index", "vocal_noise_fraction"]

class ParkinsonsDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Parkinson's Disease Acoustic Risk."""

    def __init__(self):
        super().__init__(
            name="Parkinson's Disease",
            slug="parkinsons",
            category="Neurology",
            description="Acoustic phonation analysis for early Parkinson's tremor and dysphonia detection.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "fo_hz", "data_type": "float", "min_value": 80.0, "max_value": 260.0, "unit": "Hz", "is_required": True},
            {"name": "fhi_hz", "data_type": "float", "min_value": 90.0, "max_value": 500.0, "unit": "Hz", "is_required": True},
            {"name": "flo_hz", "data_type": "float", "min_value": 60.0, "max_value": 250.0, "unit": "Hz", "is_required": True},
            {"name": "jitter_percent", "data_type": "float", "min_value": 0.001, "max_value": 0.05, "unit": "%", "is_required": True},
            {"name": "shimmer", "data_type": "float", "min_value": 0.005, "max_value": 0.15, "unit": "score", "is_required": True},
            {"name": "hnr", "data_type": "float", "min_value": 5.0, "max_value": 35.0, "unit": "dB", "is_required": True},
            {"name": "rpde", "data_type": "float", "min_value": 0.1, "max_value": 0.8, "unit": "score", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return ParkinsonsFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return ParkinsonsPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42)
        }
