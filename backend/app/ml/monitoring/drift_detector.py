"""
MedPredict AI — Feature Drift & Model Fairness Detection Engine
Implements authentic statistical tests: Kolmogorov-Smirnov (KS-test),
Population Stability Index (PSI), and Demographic Parity / Disparate Impact ratios.
"""

from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
from scipy import stats

class DriftDetector:
    """
    Evaluates covariate shift and distributional drift between reference baseline
    and observed production inference features.
    """

    @staticmethod
    def calculate_psi(
        expected: np.ndarray,
        actual: np.ndarray,
        num_buckets: int = 10
    ) -> float:
        """
        Calculates Population Stability Index (PSI) across quantile buckets.
        Formula: sum((actual_pct - expected_pct) * ln(actual_pct / expected_pct))
        """
        expected = expected[~np.isnan(expected)]
        actual = actual[~np.isnan(actual)]

        if len(expected) == 0 or len(actual) == 0:
            return 0.0

        # Create quantile bins based on reference baseline
        quantiles = np.linspace(0, 100, num_buckets + 1)
        bins = np.percentile(expected, quantiles)
        bins[0] = -np.inf
        bins[-1] = np.inf
        # Ensure strictly monotonic bins
        bins = np.unique(bins)
        if len(bins) < 2:
            return 0.0

        expected_counts, _ = np.histogram(expected, bins=bins)
        actual_counts, _ = np.histogram(actual, bins=bins)

        expected_pct = expected_counts / len(expected)
        actual_pct = actual_counts / len(actual)

        # Smooth zero counts to avoid log(0)
        epsilon = 1e-4
        expected_pct = np.where(expected_pct == 0, epsilon, expected_pct)
        actual_pct = np.where(actual_pct == 0, epsilon, actual_pct)

        # Re-normalize
        expected_pct /= np.sum(expected_pct)
        actual_pct /= np.sum(actual_pct)

        psi_val = np.sum((actual_pct - expected_pct) * np.log(actual_pct / expected_pct))
        return float(psi_val)

    @classmethod
    def evaluate_feature_drift(
        cls,
        reference_df: pd.DataFrame,
        current_df: pd.DataFrame,
        numerical_features: List[str]
    ) -> Dict[str, Any]:
        """
        Performs per-feature drift assessment using KS-test and PSI metrics.
        """
        results = {}
        drifted_features = []

        for col in numerical_features:
            if col not in reference_df.columns or col not in current_df.columns:
                continue

            ref_vals = pd.to_numeric(reference_df[col], errors='coerce').dropna().values
            curr_vals = pd.to_numeric(current_df[col], errors='coerce').dropna().values

            if len(ref_vals) < 5 or len(curr_vals) < 5:
                continue

            # Two-sample Kolmogorov-Smirnov test
            ks_res = stats.ks_2samp(ref_vals, curr_vals)
            ks_stat = round(float(ks_res.statistic), 4)
            p_value = round(float(ks_res.pvalue), 5)

            # PSI calculation
            psi = round(cls.calculate_psi(ref_vals, curr_vals), 4)

            # Interpretation: PSI < 0.1 No Change; 0.1-0.2 Moderate Drift; > 0.2 Significant Drift
            if psi > 0.2 or p_value < 0.01:
                severity = "SIGNIFICANT"
                drifted_features.append(col)
            elif psi >= 0.1 or p_value < 0.05:
                severity = "MODERATE"
                drifted_features.append(col)
            else:
                severity = "NONE"

            results[col] = {
                "ks_statistic": ks_stat,
                "p_value": p_value,
                "psi": psi,
                "severity": severity,
                "ref_mean": round(float(np.mean(ref_vals)), 3),
                "curr_mean": round(float(np.mean(curr_vals)), 3),
                "ref_std": round(float(np.std(ref_vals)), 3),
                "curr_std": round(float(np.std(curr_vals)), 3),
            }

        overall_drift = len(drifted_features) > 0

        return {
            "overall_drift_detected": overall_drift,
            "drifted_features_count": len(drifted_features),
            "drifted_features": drifted_features,
            "feature_metrics": results
        }

    @staticmethod
    def evaluate_fairness(
        predictions: List[int],
        sensitive_attribute: List[Any],
        privileged_value: Any,
        unprivileged_value: Any
    ) -> Dict[str, Any]:
        """
        Evaluates algorithmic fairness metrics:
        - Demographic Parity Difference: |P(Y=1|unprivileged) - P(Y=1|privileged)|
        - Disparate Impact Ratio: P(Y=1|unprivileged) / P(Y=1|privileged)
        """
        preds = np.array(predictions)
        sens = np.array(sensitive_attribute)

        priv_mask = (sens == privileged_value)
        unpriv_mask = (sens == unprivileged_value)

        priv_count = np.sum(priv_mask)
        unpriv_count = np.sum(unpriv_mask)

        if priv_count == 0 or unpriv_count == 0:
            return {
                "valid": False,
                "message": "Insufficient sample size across sensitive demographic subgroups."
            }

        priv_pos_rate = float(np.mean(preds[priv_mask]))
        unpriv_pos_rate = float(np.mean(preds[unpriv_mask]))

        parity_diff = abs(unpriv_pos_rate - priv_pos_rate)
        
        if priv_pos_rate > 0:
            disparate_impact = unpriv_pos_rate / priv_pos_rate
        else:
            disparate_impact = 1.0

        # EEOC 80% four-fifths rule threshold
        fairness_flag = disparate_impact >= 0.80 and disparate_impact <= 1.25

        return {
            "valid": True,
            "privileged_group": str(privileged_value),
            "unprivileged_group": str(unprivileged_value),
            "privileged_positive_rate": round(priv_pos_rate, 4),
            "unprivileged_positive_rate": round(unpriv_pos_rate, 4),
            "demographic_parity_difference": round(parity_diff, 4),
            "disparate_impact_ratio": round(disparate_impact, 4),
            "satisfies_80_percent_rule": fairness_flag
        }
