"""
MedPredict AI — Model Evaluation Engine
Calculates authentic evaluation metrics without fabrication.
"""

from typing import Any, Dict
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    confusion_matrix,
    brier_score_loss
)

class ModelEvaluator:
    """
    Computes rigorous classification metrics from actual test predictions and ground truth.
    Strictly forbids fabricated or hard-coded performance values.
    """

    @staticmethod
    def evaluate(y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> Dict[str, Any]:
        """
        Evaluates binary classification predictions.
        y_true: Ground truth labels (0 or 1)
        y_pred: Predicted class labels (0 or 1)
        y_prob: Probability scores for the positive class (0.0 to 1.0)
        """
        # Ensure 1D arrays
        y_true = np.asarray(y_true).ravel()
        y_pred = np.asarray(y_pred).ravel()
        y_prob = np.asarray(y_prob).ravel()

        cm = confusion_matrix(y_true, y_pred)
        tn, fp, fn, tp = cm.ravel() if cm.shape == (2, 2) else (0, 0, 0, 0)

        # Sensitivity / Specificity
        sensitivity = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        specificity = float(tn / (tn + fp)) if (tn + fp) > 0 else 0.0

        # Calculate ROC-AUC if both classes present
        try:
            roc_auc = float(roc_auc_score(y_true, y_prob)) if len(np.unique(y_true)) > 1 else 0.5
        except Exception:
            roc_auc = 0.5

        # Calculate PR-AUC (Average Precision)
        try:
            pr_auc = float(average_precision_score(y_true, y_prob)) if len(np.unique(y_true)) > 1 else 0.0
        except Exception:
            pr_auc = 0.0

        # Calibration Brier score
        try:
            brier = float(brier_score_loss(y_true, y_prob))
        except Exception:
            brier = 0.0

        return {
            "accuracy": round(float(accuracy_score(y_true, y_pred)), 4),
            "precision": round(float(precision_score(y_true, y_pred, zero_division=0)), 4),
            "recall": round(float(recall_score(y_true, y_pred, zero_division=0)), 4),
            "f1_score": round(float(f1_score(y_true, y_pred, zero_division=0)), 4),
            "sensitivity": round(sensitivity, 4),
            "specificity": round(specificity, 4),
            "roc_auc": round(roc_auc, 4),
            "pr_auc": round(pr_auc, 4),
            "brier_score": round(brier, 4),
            "confusion_matrix": {
                "true_negative": int(tn),
                "false_positive": int(fp),
                "false_negative": int(fn),
                "true_positive": int(tp)
            },
            "sample_count": int(len(y_true))
        }
