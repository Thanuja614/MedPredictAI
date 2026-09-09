"""
MedPredict AI — Base Risk Predictor & Classification Engine
Computes model probabilities and maps them to configurable risk bands with safety messaging.
"""

from typing import Any, Dict, List
import numpy as np

MEDICAL_SAFETY_DISCLAIMER = (
    "This prediction is intended for educational, research and decision-support purposes only. "
    "It is not a medical diagnosis and should not replace advice from a qualified healthcare professional."
)

class BasePredictor:
    """
    Encapsulates inference execution, probability calibration, and risk banding.
    """

    def __init__(
        self,
        model: Any,
        preprocessor: Any,
        feature_names: List[str],
        moderate_threshold: float = 0.35,
        high_threshold: float = 0.70
    ):
        self.model = model
        self.preprocessor = preprocessor
        self.feature_names = feature_names
        self.moderate_threshold = moderate_threshold
        self.high_threshold = high_threshold

    def classify_risk(self, probability: float) -> str:
        """Categorizes probability into configurable system risk categories."""
        if probability < self.moderate_threshold:
            return "LOW"
        elif probability < self.high_threshold:
            return "MODERATE"
        else:
            return "HIGH"

    def predict_risk(self, input_features: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes inference for a patient input dictionary.
        Returns probability, risk level, and medical safety disclaimer.
        """
        # Format into ordered row DataFrame or array
        import pandas as pd
        df = pd.DataFrame([input_features])
        
        # Ensure all required features are present
        for col in self.feature_names:
            if col not in df.columns:
                raise ValueError(f"Missing required feature: '{col}'")

        # Select only required columns in strict order
        df = df[self.feature_names]

        # Preprocess
        df_processed = self.preprocessor.transform(df)

        # Predict probability
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(df_processed)
            prob_positive = float(probs[0, 1])
        elif hasattr(self.model, "decision_function"):
            # Normalize decision function via sigmoid
            df_val = self.model.decision_function(df_processed)[0]
            prob_positive = float(1.0 / (1.0 + np.exp(-df_val)))
        else:
            # Fallback to binary predict
            prob_positive = float(self.model.predict(df_processed)[0])

        risk_level = self.classify_risk(prob_positive)

        return {
            "probability": round(prob_positive, 4),
            "risk_level": risk_level,
            "thresholds": {
                "moderate_cutoff": self.moderate_threshold,
                "high_cutoff": self.high_threshold
            },
            "disclaimer": MEDICAL_SAFETY_DISCLAIMER
        }
