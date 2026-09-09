"""
MedPredict AI — Heart Disease Prediction Module (Phase 10)
Implements cardiovascular data processing, clinical feature engineering,
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
    "chest_pain_type",
    "resting_bp",
    "cholesterol",
    "fasting_blood_sugar",
    "resting_ecg",
    "max_hr",
    "exercise_angina",
    "st_depression",
    "st_slope"
]

class HeartPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and standard scaling for hemodynamic parameters."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "HeartPreprocessor":
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

class HeartFeatureEngineer(BaseFeatureEngineer):
    """
    Derives cardiovascular risk indices:
    - Rate Pressure Product (RPP proxy): (max_hr * resting_bp) / 100.0
    - Cholesterol to Age Index: cholesterol / (age + 1e-5)
    - Hypercholesterolemia indicator: cholesterol >= 240 mg/dL
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["rate_pressure_product"] = (df_out["max_hr"] * df_out["resting_bp"]) / 100.0
        df_out["cholesterol_age_index"] = df_out["cholesterol"] / (df_out["age"] + 1e-5)
        df_out["high_cholesterol_flag"] = (df_out["cholesterol"] >= 240.0).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["rate_pressure_product", "cholesterol_age_index", "high_cholesterol_flag"]

class HeartDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Coronary Artery & Heart Disease Risk."""

    def __init__(self):
        super().__init__(
            name="Heart Disease",
            slug="heart",
            category="Cardiovascular",
            description="Coronary artery disease risk estimation using hemodynamic and electrocardiographic markers.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "age", "data_type": "integer", "min_value": 20, "max_value": 100, "unit": "years", "is_required": True},
            {"name": "sex", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "code", "is_required": True},
            {"name": "chest_pain_type", "data_type": "categorical", "min_value": 0, "max_value": 3, "unit": "code", "is_required": True},
            {"name": "resting_bp", "data_type": "float", "min_value": 80.0, "max_value": 220.0, "unit": "mmHg", "is_required": True},
            {"name": "cholesterol", "data_type": "float", "min_value": 100.0, "max_value": 600.0, "unit": "mg/dL", "is_required": True},
            {"name": "fasting_blood_sugar", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "resting_ecg", "data_type": "categorical", "min_value": 0, "max_value": 2, "unit": "code", "is_required": True},
            {"name": "max_hr", "data_type": "float", "min_value": 60.0, "max_value": 220.0, "unit": "bpm", "is_required": True},
            {"name": "exercise_angina", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "st_depression", "data_type": "float", "min_value": 0.0, "max_value": 7.0, "unit": "mm", "is_required": True},
            {"name": "st_slope", "data_type": "categorical", "min_value": 0, "max_value": 2, "unit": "code", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return HeartFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return HeartPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        }
