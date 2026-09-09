"""
MedPredict AI — Stroke Prediction Module (Phase 14)
Implements cerebrovascular data processing, vascular comorbidity scoring,
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
    "gender",
    "age",
    "hypertension",
    "heart_disease",
    "ever_married",
    "avg_glucose_level",
    "bmi"
]

class StrokePreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for stroke demographic and metabolic markers."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="stroke")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "StrokePreprocessor":
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

class StrokeFeatureEngineer(BaseFeatureEngineer):
    """
    Derives cerebrovascular risk indicators:
    - Vascular Comorbidity Score: (hypertension * 1.5) + (heart_disease * 2.0)
    - Glycemic Age Interaction: (avg_glucose_level * age) / 100.0
    - Obesity Risk Factor: bmi >= 30.0 kg/m^2
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["comorbidity_score"] = (df_out["hypertension"] * 1.5) + (df_out["heart_disease"] * 2.0)
        df_out["glucose_age_interaction"] = (df_out["avg_glucose_level"] * df_out["age"]) / 100.0
        df_out["obesity_risk_flag"] = (df_out["bmi"] >= 30.0).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["comorbidity_score", "glucose_age_interaction", "obesity_risk_flag"]

class StrokeDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Stroke Risk."""

    def __init__(self):
        super().__init__(
            name="Stroke",
            slug="stroke",
            category="Neurology & Cerebrovascular",
            description="Cerebrovascular accident risk estimation using hemodynamic and metabolic indicators.",
            target_column="stroke",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "gender", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "code", "is_required": True},
            {"name": "age", "data_type": "float", "min_value": 18.0, "max_value": 100.0, "unit": "years", "is_required": True},
            {"name": "hypertension", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "heart_disease", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "ever_married", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "flag", "is_required": True},
            {"name": "avg_glucose_level", "data_type": "float", "min_value": 50.0, "max_value": 300.0, "unit": "mg/dL", "is_required": True},
            {"name": "bmi", "data_type": "float", "min_value": 12.0, "max_value": 65.0, "unit": "kg/m^2", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return StrokeFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return StrokePreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42)
        }
