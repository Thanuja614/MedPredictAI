"""
MedPredict AI — Diabetes Prediction Module (Phase 9)
Implements end-to-end data processing, clinical feature engineering,
model training, risk prediction, and local explainability for Type-2 Diabetes.
"""

from typing import Any, Dict, List
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from backend.app.ml.framework.base_preprocessor import BasePreprocessor
from backend.app.ml.framework.base_feature_engineer import BaseFeatureEngineer
from backend.app.ml.framework.base_module import BaseDiseaseModule

RAW_FEATURES = [
    "pregnancies",
    "glucose",
    "blood_pressure",
    "skin_thickness",
    "insulin",
    "bmi",
    "diabetes_pedigree",
    "age"
]

class DiabetesPreprocessor(BasePreprocessor):
    """
    Imputes zero-replacement biological markers and applies standard scaling.
    Fitted strictly on training data without leakage.
    """

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="outcome")
        self.imputer = SimpleImputer(missing_values=0.0, strategy="median")
        self.scaler = StandardScaler()
        # Features where 0 is physiologically invalid and represents missing data
        self.zero_as_missing_cols = ["glucose", "blood_pressure", "skin_thickness", "insulin", "bmi"]

    def fit(self, df: pd.DataFrame) -> "DiabetesPreprocessor":
        df_copy = df[self.feature_names].copy()
        
        # Replace 0 with NaN for specific physiological biomarkers
        for col in self.zero_as_missing_cols:
            if col in df_copy.columns:
                df_copy[col] = df_copy[col].replace(0.0, np.nan)
        
        # Compute median statistics on train
        self.medians = {col: float(df_copy[col].median(skipna=True)) for col in self.feature_names}
        df_imputed = df_copy.fillna(self.medians)

        self.scaler.fit(df_imputed)
        self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.check_fitted()
        df_copy = df[self.feature_names].copy()
        
        for col in self.zero_as_missing_cols:
            if col in df_copy.columns:
                df_copy[col] = df_copy[col].replace(0.0, np.nan)

        df_imputed = df_copy.fillna(self.medians)
        scaled_array = self.scaler.transform(df_imputed)
        return pd.DataFrame(scaled_array, columns=self.feature_names, index=df.index)

class DiabetesFeatureEngineer(BaseFeatureEngineer):
    """
    Derives clinical indicators:
    - Insulin Resistance Proxy: (glucose * insulin) / 405.0
    - Metabolic Load Ratio: glucose / (bmi + 1e-5)
    - High-Risk Age Category: age >= 45 (1 or 0)
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["insulin_resistance_index"] = (df_out["glucose"] * df_out["insulin"]) / 405.0
        df_out["metabolic_load_ratio"] = df_out["glucose"] / (df_out["bmi"] + 1e-5)
        df_out["age_risk_factor"] = (df_out["age"] >= 45).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["insulin_resistance_index", "metabolic_load_ratio", "age_risk_factor"]

class DiabetesDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Type-2 Diabetes Risk."""

    def __init__(self):
        super().__init__(
            name="Diabetes",
            slug="diabetes",
            category="Endocrine & Metabolic",
            description="Type-2 Diabetes risk screening model using glycemic and metabolic markers.",
            target_column="outcome",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "pregnancies", "data_type": "integer", "min_value": 0, "max_value": 20, "unit": "count", "is_required": True},
            {"name": "glucose", "data_type": "float", "min_value": 40.0, "max_value": 300.0, "unit": "mg/dL", "is_required": True},
            {"name": "blood_pressure", "data_type": "float", "min_value": 40.0, "max_value": 200.0, "unit": "mmHg", "is_required": True},
            {"name": "skin_thickness", "data_type": "float", "min_value": 5.0, "max_value": 100.0, "unit": "mm", "is_required": True},
            {"name": "insulin", "data_type": "float", "min_value": 10.0, "max_value": 900.0, "unit": "mu U/ml", "is_required": True},
            {"name": "bmi", "data_type": "float", "min_value": 15.0, "max_value": 60.0, "unit": "kg/m^2", "is_required": True},
            {"name": "diabetes_pedigree", "data_type": "float", "min_value": 0.05, "max_value": 2.5, "unit": "score", "is_required": True},
            {"name": "age", "data_type": "integer", "min_value": 18, "max_value": 100, "unit": "years", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return DiabetesFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return DiabetesPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        }
