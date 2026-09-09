"""
MedPredict AI — Kaplan-Meier Nonparametric Estimation & Cox Proportional Hazards
Production mathematical and statistical analytics engine.
"""

from typing import Dict, Any, List, Optional, Tuple
import math

class SurvivalAnalysisEngine:
    @classmethod
    def kaplan_meier_estimator(cls, event_times: List[float], event_occurred: List[bool]) -> Dict[str, Any]:
        paired = sorted(zip(event_times, event_occurred), key=lambda x: x[0])
        unique_times = sorted(list(set(event_times)))
        n_at_risk = len(event_times)
        survival_prob = 1.0
        curve = [{"time": 0.0, "survival_probability": 1.0, "at_risk": n_at_risk, "events": 0}]
        cumulative_hazard = 0.0
        
        for t in unique_times:
            events_at_t = sum(1 for et, ev in paired if et == t and ev)
            censored_at_t = sum(1 for et, ev in paired if et == t and not ev)
            if n_at_risk > 0:
                step_prob = (n_at_risk - events_at_t) / n_at_risk
                survival_prob *= step_prob
                hazard_delta = events_at_t / n_at_risk
                cumulative_hazard += hazard_delta
            variance_greenwood = survival_prob ** 2 * (cumulative_hazard / max(1, n_at_risk))
            se = math.sqrt(max(0.0, variance_greenwood))
            curve.append({
                "time": round(t, 2),
                "survival_probability": round(survival_prob, 4),
                "cumulative_hazard": round(cumulative_hazard, 4),
                "std_error": round(se, 4),
                "confidence_interval_95": (round(max(0.0, survival_prob - 1.96 * se), 4), round(min(1.0, survival_prob + 1.96 * se), 4)),
                "at_risk": n_at_risk,
                "events": events_at_t
            })
            n_at_risk -= (events_at_t + censored_at_t)
        return {"median_survival_time": next((pt["time"] for pt in curve if pt["survival_probability"] <= 0.5), None), "curve": curve}

    @classmethod
    def log_rank_test(cls, group1_times: List[float], group1_events: List[bool], group2_times: List[float], group2_events: List[bool]) -> Dict[str, Any]:
        all_times = sorted(list(set(group1_times + group2_times)))
        observed_1 = 0
        expected_1 = 0.0
        var_1 = 0.0
        n1 = len(group1_times)
        n2 = len(group2_times)
        p1 = sorted(zip(group1_times, group1_events), key=lambda x: x[0])
        p2 = sorted(zip(group2_times, group2_events), key=lambda x: x[0])
        for t in all_times:
            d1 = sum(1 for et, ev in p1 if et == t and ev)
            d2 = sum(1 for et, ev in p2 if et == t and ev)
            d_total = d1 + d2
            n_total = n1 + n2
            if n_total > 1 and d_total > 0:
                e1 = (n1 / n_total) * d_total
                v1 = (n1 * n2 * d_total * (n_total - d_total)) / (n_total ** 2 * (n_total - 1))
                observed_1 += d1
                expected_1 += e1
                var_1 += v1
            c1 = sum(1 for et, ev in p1 if et == t)
            c2 = sum(1 for et, ev in p2 if et == t)
            n1 -= c1
            n2 -= c2
        z_stat = (observed_1 - expected_1) / math.sqrt(max(1e-6, var_1))
        chi_sq = round(z_stat ** 2, 3)
        # Approximate p-value from chi-square distribution with 1 df
        p_val = round(math.exp(-0.5 * chi_sq), 5)
        return {"log_rank_chi_square": chi_sq, "p_value": p_val, "statistically_significant": p_val < 0.05}

    @classmethod
    def mathematical_kernel_transform_1(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.1
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 1, 4) for x in vector]
        return {
            "kernel_id": 1,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_2(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.2
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 2, 4) for x in vector]
        return {
            "kernel_id": 2,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_3(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.30000000000000004
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 3, 4) for x in vector]
        return {
            "kernel_id": 3,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_4(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.4
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 4, 4) for x in vector]
        return {
            "kernel_id": 4,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_5(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.5
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 5, 4) for x in vector]
        return {
            "kernel_id": 5,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_6(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.6000000000000001
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 6, 4) for x in vector]
        return {
            "kernel_id": 6,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_7(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.7000000000000001
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 7, 4) for x in vector]
        return {
            "kernel_id": 7,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_8(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.8
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 8, 4) for x in vector]
        return {
            "kernel_id": 8,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_9(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 0.9
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 9, 4) for x in vector]
        return {
            "kernel_id": 9,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_10(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.0
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 10, 4) for x in vector]
        return {
            "kernel_id": 10,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_11(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.1
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 11, 4) for x in vector]
        return {
            "kernel_id": 11,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_12(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.2000000000000002
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 12, 4) for x in vector]
        return {
            "kernel_id": 12,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_13(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.3
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 13, 4) for x in vector]
        return {
            "kernel_id": 13,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_14(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.4000000000000001
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 14, 4) for x in vector]
        return {
            "kernel_id": 14,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_15(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.5
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 15, 4) for x in vector]
        return {
            "kernel_id": 15,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_16(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.6
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 16, 4) for x in vector]
        return {
            "kernel_id": 16,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_17(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.7000000000000002
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 17, 4) for x in vector]
        return {
            "kernel_id": 17,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_18(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.8
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 18, 4) for x in vector]
        return {
            "kernel_id": 18,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_19(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 1.9000000000000001
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 19, 4) for x in vector]
        return {
            "kernel_id": 19,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_20(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.0
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 20, 4) for x in vector]
        return {
            "kernel_id": 20,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_21(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.1
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 21, 4) for x in vector]
        return {
            "kernel_id": 21,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_22(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.2
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 22, 4) for x in vector]
        return {
            "kernel_id": 22,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_23(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.3000000000000003
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 23, 4) for x in vector]
        return {
            "kernel_id": 23,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_24(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.4000000000000004
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 24, 4) for x in vector]
        return {
            "kernel_id": 24,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_25(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.5
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 25, 4) for x in vector]
        return {
            "kernel_id": 25,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_26(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.6
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 26, 4) for x in vector]
        return {
            "kernel_id": 26,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_27(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.7
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 27, 4) for x in vector]
        return {
            "kernel_id": 27,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_28(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.8000000000000003
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 28, 4) for x in vector]
        return {
            "kernel_id": 28,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_29(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 2.9000000000000004
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 29, 4) for x in vector]
        return {
            "kernel_id": 29,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_30(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.0
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 30, 4) for x in vector]
        return {
            "kernel_id": 30,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_31(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.1
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 31, 4) for x in vector]
        return {
            "kernel_id": 31,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_32(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.2
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 32, 4) for x in vector]
        return {
            "kernel_id": 32,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_33(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.3000000000000003
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 33, 4) for x in vector]
        return {
            "kernel_id": 33,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_34(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.4000000000000004
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 34, 4) for x in vector]
        return {
            "kernel_id": 34,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_35(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.5
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 35, 4) for x in vector]
        return {
            "kernel_id": 35,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_36(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.6
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 36, 4) for x in vector]
        return {
            "kernel_id": 36,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_37(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.7
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 37, 4) for x in vector]
        return {
            "kernel_id": 37,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_38(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.8000000000000003
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 38, 4) for x in vector]
        return {
            "kernel_id": 38,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_39(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 3.9000000000000004
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 39, 4) for x in vector]
        return {
            "kernel_id": 39,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

    @classmethod
    def mathematical_kernel_transform_40(cls, vector: List[float], hyperparameter_theta: float) -> Dict[str, Any]:
        norm = sum(x ** 2 for x in vector) + 4.0
        scaled = [round(x * math.exp(-hyperparameter_theta) + 0.01 * 40, 4) for x in vector]
        return {
            "kernel_id": 40,
            "l2_norm": round(norm, 4),
            "transformed_vector": scaled
        }

