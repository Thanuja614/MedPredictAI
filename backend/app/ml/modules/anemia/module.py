"""
MedPredict AI — Anemia Screening Module (Phase 16)
Implements hematologic data processing, Mentzer Index & microcytic erythrocyte engineering,
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
    "hemoglobin",
    "mch",
    "mchc",
    "mcv"
]

class AnemiaPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for complete blood count (CBC) indices."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "AnemiaPreprocessor":
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

class AnemiaFeatureEngineer(BaseFeatureEngineer):
    """
    Derives clinical hematologic indicators:
    - Mentzer Index Proxy: mcv / (hemoglobin + 1e-5)
    - Hemoglobin Deficit: max(0.0, 13.5 - hemoglobin)
    - Microcytic Indicator: mcv < 80.0 fL
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["mentzer_index_proxy"] = df_out["mcv"] / (df_out["hemoglobin"] + 1e-5)
        df_out["hemoglobin_deficit"] = (13.5 - df_out["hemoglobin"]).clip(lower=0.0)
        df_out["microcytic_flag"] = (df_out["mcv"] < 80.0).astype(float)
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["mentzer_index_proxy", "hemoglobin_deficit", "microcytic_flag"]

class AnemiaDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Anemia Deficiency Risk."""

    def __init__(self):
        super().__init__(
            name="Anemia",
            slug="anemia",
            category="Hematology",
            description="Erythrocyte and hemoglobin deficiency screening from complete blood count metrics.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "gender", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "code", "is_required": True},
            {"name": "hemoglobin", "data_type": "float", "min_value": 4.0, "max_value": 20.0, "unit": "g/dL", "is_required": True},
            {"name": "mch", "data_type": "float", "min_value": 12.0, "max_value": 40.0, "unit": "pg", "is_required": True},
            {"name": "mchc", "data_type": "float", "min_value": 20.0, "max_value": 40.0, "unit": "g/dL", "is_required": True},
            {"name": "mcv", "data_type": "float", "min_value": 50.0, "max_value": 120.0, "unit": "fL", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return AnemiaFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return AnemiaPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        }
