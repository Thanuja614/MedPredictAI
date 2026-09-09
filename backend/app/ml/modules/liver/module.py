"""
MedPredict AI — Liver Disease Prediction Module (Phase 11)
Implements hepatic biomarker processing, De Ritis ratio (AST/ALT) engineering,
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
    "gender",
    "total_bilirubin",
    "direct_bilirubin",
    "alkaline_phosphatase",
    "alamine_aminotransferase",
    "aspartate_aminotransferase",
    "total_proteins",
    "albumin",
    "ag_ratio"
]

class LiverPreprocessor(BasePreprocessor):
    """Encapsulates median imputation and scaling for hepatic enzymes and proteins."""

    def __init__(self, feature_names: List[str]):
        super().__init__(feature_names, target_name="target")
        self.scaler = StandardScaler()
        self.medians: Dict[str, float] = {}

    def fit(self, df: pd.DataFrame) -> "LiverPreprocessor":
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

class LiverFeatureEngineer(BaseFeatureEngineer):
    """
    Derives clinical hepatic indicators:
    - De Ritis Ratio: AST / (ALT + 1e-5) (Classic biomarker for hepatic injury)
    - Conjugated Bilirubin Ratio: direct_bilirubin / (total_bilirubin + 1e-5)
    - Calculated Globulin: total_proteins - albumin
    """

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["de_ritis_ratio"] = df_out["aspartate_aminotransferase"] / (df_out["alamine_aminotransferase"] + 1e-5)
        df_out["direct_bilirubin_ratio"] = df_out["direct_bilirubin"] / (df_out["total_bilirubin"] + 1e-5)
        df_out["calculated_globulin"] = df_out["total_proteins"] - df_out["albumin"]
        return df_out

    def get_engineered_feature_names(self) -> List[str]:
        return ["de_ritis_ratio", "direct_bilirubin_ratio", "calculated_globulin"]

class LiverDiseaseModule(BaseDiseaseModule):
    """Production Disease Module for Liver Disease Risk."""

    def __init__(self):
        super().__init__(
            name="Liver Disease",
            slug="liver",
            category="Gastroenterology & Hepatology",
            description="Hepatic impairment risk evaluation from liver enzymes and protein fractions.",
            target_column="target",
            raw_features=RAW_FEATURES,
            version="1.0.0"
        )

    def get_feature_schema(self) -> List[Dict[str, Any]]:
        return [
            {"name": "age", "data_type": "integer", "min_value": 10, "max_value": 100, "unit": "years", "is_required": True},
            {"name": "gender", "data_type": "categorical", "min_value": 0, "max_value": 1, "unit": "code", "is_required": True},
            {"name": "total_bilirubin", "data_type": "float", "min_value": 0.2, "max_value": 30.0, "unit": "mg/dL", "is_required": True},
            {"name": "direct_bilirubin", "data_type": "float", "min_value": 0.1, "max_value": 15.0, "unit": "mg/dL", "is_required": True},
            {"name": "alkaline_phosphatase", "data_type": "float", "min_value": 50.0, "max_value": 2000.0, "unit": "IU/L", "is_required": True},
            {"name": "alamine_aminotransferase", "data_type": "float", "min_value": 5.0, "max_value": 1500.0, "unit": "IU/L", "is_required": True},
            {"name": "aspartate_aminotransferase", "data_type": "float", "min_value": 5.0, "max_value": 1500.0, "unit": "IU/L", "is_required": True},
            {"name": "total_proteins", "data_type": "float", "min_value": 2.0, "max_value": 10.0, "unit": "g/dL", "is_required": True},
            {"name": "albumin", "data_type": "float", "min_value": 1.0, "max_value": 6.0, "unit": "g/dL", "is_required": True},
            {"name": "ag_ratio", "data_type": "float", "min_value": 0.2, "max_value": 3.0, "unit": "ratio", "is_required": True}
        ]

    def build_feature_engineer(self) -> BaseFeatureEngineer:
        return LiverFeatureEngineer()

    def build_preprocessor(self) -> BasePreprocessor:
        all_features = self.raw_features + self.build_feature_engineer().get_engineered_feature_names()
        return LiverPreprocessor(all_features)

    def get_candidate_models(self) -> Dict[str, Any]:
        return {
            "random_forest": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42)
        }
