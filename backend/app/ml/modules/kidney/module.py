"""
MedPredict AI — Chronic Kidney Disease (CKD) Module (Phase 12)
Implements renal biomarker processing, BUN/Creatinine ratio engineering,
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
    "blood_pressure",
    "specific_gravity",
    "albumin",
    "sugar",
    "blood_urea",
    "serum_creatinine",
    "sodium",
    "potassium",
    "hemoglobin"
]

class KidneyPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for renal functional markers."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "KidneyPreprocessor":
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

class KidneyFeatureEngineer(BaseFeatureEngineer):
    """
    Derives clinical renal indicators:
    - BUN to Creatinine Ratio: blood_urea / (serum_creatinine + 1e-5) (Prerenal vs Intrinsic Azotemia)
    - Sodium to Potassium Balance: sodium / (potassium + 1e-5)
    - Renal Anemia Flag: hemoglobin < 11.0 g/dL
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["bun_creatinine_ratio"] = df_out["blood_urea"] / (df_out["serum_creatinine"] + 1e-5)
        df_out["electrolyte_balance"] = df_out["sodium"] / (df_out["potassium"] + 1e-5)
        df_out["renal_anemia_flag"] = (df_out["hemoglobin"] < 11.0).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["bun_creatinine_ratio", "electrolyte_balance", "renal_anemia_flag"]

class KidneyDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Chronic Kidney Disease (CKD)."""

    def __init__(self):
        super().__init__(
            name="Kidney Disease",
            slug="kidney",
            category="Nephrology",
            description="Chronic kidney disease staging and risk detection using metabolic markers.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "age", "data_type": "integer", "min_value": 10, "max_value": 100, "unit": "years", "is_required": True},
            {"name": "blood_pressure", "data_type": "float", "min_value": 50.0, "max_value": 200.0, "unit": "mmHg", "is_required": True},
            {"name": "specific_gravity", "data_type": "float", "min_value": 1.005, "max_value": 1.030, "unit": "sg", "is_required": True},
            {"name": "albumin", "data_type": "integer", "min_value": 0, "max_value": 5, "unit": "grade", "is_required": True},
            {"name": "sugar", "data_type": "integer", "min_value": 0, "max_value": 5, "unit": "grade", "is_required": True},
            {"name": "blood_urea", "data_type": "float", "min_value": 10.0, "max_value": 300.0, "unit": "mg/dL", "is_required": True},
            {"name": "serum_creatinine", "data_type": "float", "min_value": 0.4, "max_value": 15.0, "unit": "mg/dL", "is_required": True},
            {"name": "sodium", "data_type": "float", "min_value": 100.0, "max_value": 170.0, "unit": "mEq/L", "is_required": True},
            {"name": "potassium", "data_type": "float", "min_value": 2.0, "max_value": 8.0, "unit": "mEq/L", "is_required": True},
            {"name": "hemoglobin", "data_type": "float", "min_value": 3.0, "max_value": 18.0, "unit": "g/dL", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return KidneyFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return KidneyPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42)
        }
