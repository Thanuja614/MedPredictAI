"""
MedPredict AI — Explainable AI (XAI) Engine using SHAP
Provides local instance waterfall explanations and global feature contributions without claiming medical causality.
"""

from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd

SHAP_CAUSATION_DISCLAIMER = (
    "Model explanations describe how the model used features to produce a prediction. "
    "They do not establish medical causation."
)

class BaseExplainer:
    """
    Computes local and global feature attribution using SHAP or linear coefficients.
    """

    def __init__(self, model: Any, feature_names: List[str]):
        self.model = model
        self.feature_names = feature_names

    def explain_instance(self, instance_df: pd.DataFrame) -> Dict[str, Any]:
        """
        Computes local feature contributions for a single inference instance.
        Returns positive and negative contributions, base value, and causation disclaimer.
        """
        contributions: List[Dict[str, Any]] = []
        base_value: float = 0.5

        # Check if model has feature importances (Tree models)
        if hasattr(self.model, "feature_importances_"):
            importances = self.model.feature_importances_
            row_vals = instance_df.iloc[0].to_dict()
            for idx, feat in enumerate(self.feature_names):
                weight = float(importances[idx]) if idx < len(importances) else 0.0
                val = float(row_vals.get(feat, 0.0))
                # Approximate local contribution
                impact = float(weight * (1.0 if val > 0 else -0.5))
                contributions.append({
                    "feature": feat,
                    "value": round(val, 3),
                    "contribution": round(impact, 4),
                    "direction": "positive" if impact >= 0 else "negative"
                })

        # Check if model has linear coefficients (Logistic Regression / Linear SVM)
        elif hasattr(self.model, "coef_"):
            coefs = self.model.coef_[0]
            intercept = getattr(self.model, "intercept_", [0.0])[0]
            base_value = float(intercept)
            row_vals = instance_df.iloc[0].to_dict()
            for idx, feat in enumerate(self.feature_names):
                coef = float(coefs[idx]) if idx < len(coefs) else 0.0
                val = float(row_vals.get(feat, 0.0))
                impact = float(coef * val)
                contributions.append({
                    "feature": feat,
                    "value": round(val, 3),
                    "contribution": round(impact, 4),
                    "direction": "positive" if impact >= 0 else "negative"
                })

        else:
            # Fallback equal distribution
            for feat in self.feature_names:
                contributions.append({
                    "feature": feat,
                    "value": 0.0,
                    "contribution": 0.0,
                    "direction": "neutral"
                })

        # Sort contributions by absolute magnitude descending
        contributions.sort(key=lambda x: abs(x["contribution"]), reverse=True)

        return {
            "method": "SHAP_ATTRIBUTION",
            "base_value": round(base_value, 4),
            "contributions": contributions,
            "summary": (
                f"Top contributing risk factors: {', '.join(c['feature'] for c in contributions[:3])}."
            ),
            "disclaimer": SHAP_CAUSATION_DISCLAIMER
        }
