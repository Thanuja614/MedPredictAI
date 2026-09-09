"""
MedPredict AI — Hypertension Prediction Module (Phase 15)
Implements hemodynamic data processing, Pulse Pressure & Mean Arterial Pressure (MAP) engineering,
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
    "systolic_bp",
    "diastolic_bp",
    "heart_rate",
    "bmi",
    "cholesterol"
]

class HypertensionPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for hemodynamic parameters."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "HypertensionPreprocessor":
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

class HypertensionFeatureEngineer(BaseFeatureEngineer):
    """
    Derives essential hemodynamic indicators:
    - Pulse Pressure: systolic_bp - diastolic_bp (Index of vascular stiffness)
    - Mean Arterial Pressure (MAP): diastolic_bp + (pulse_pressure / 3.0)
    - Cardiological Metabolic Index: (bmi * cholesterol) / 1000.0
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        pulse_press = df_out["systolic_bp"] - df_out["diastolic_bp"]
        df_out["pulse_pressure"] = pulse_press
        df_out["mean_arterial_pressure"] = df_out["diastolic_bp"] + (pulse_press / 3.0)
        df_out["cardio_metabolic_index"] = (df_out["bmi"] * df_out["cholesterol"]) / 1000.0
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["pulse_pressure", "mean_arterial_pressure", "cardio_metabolic_index"]

class HypertensionDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Essential Hypertension Risk."""

    def __init__(self):
        super().__init__(
            name="Hypertension",
            slug="hypertension",
            category="Cardiovascular",
            description="Essential hypertension screening based on hemodynamic and anthropometric markers.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "age", "data_type": "integer", "min_value": 18, "max_value": 100, "unit": "years", "is_required": True},
            {"name": "systolic_bp", "data_type": "float", "min_value": 80.0, "max_value": 240.0, "unit": "mmHg", "is_required": True},
            {"name": "diastolic_bp", "data_type": "float", "min_value": 50.0, "max_value": 140.0, "unit": "mmHg", "is_required": True},
            {"name": "heart_rate", "data_type": "float", "min_value": 45.0, "max_value": 180.0, "unit": "bpm", "is_required": True},
            {"name": "bmi", "data_type": "float", "min_value": 15.0, "max_value": 55.0, "unit": "kg/m^2", "is_required": True},
            {"name": "cholesterol", "data_type": "float", "min_value": 100.0, "max_value": 400.0, "unit": "mg/dL", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return HypertensionFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return HypertensionPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        }
