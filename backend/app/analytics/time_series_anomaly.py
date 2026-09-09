"""
MedPredict AI — Statistical Process Control & Sequential CUSUM Change-Point Detection
Production mathematical and statistical analytics engine.
"""

from typing import Dict, Any, List, Optional, Tuple
import math

class BiomarkerAnomalyDetector:
    @classmethod
    def cusum_drift_detection(cls, series: List[float], baseline_mean: float, baseline_std: float, allowance_k: float = 0.5, decision_h: float = 4.0) -> Dict[str, Any]:
        c_pos = 0.0
        c_neg = 0.0
        anomalies = []
        for i, val in enumerate(series):
            z = (val - baseline_mean) / max(1e-6, baseline_std)
            c_pos = max(0.0, c_pos + z - allowance_k)
            c_neg = max(0.0, c_neg - z - allowance_k)
            is_alarm = c_pos > decision_h or c_neg > decision_h
            if is_alarm:
                anomalies.append({
                    "index": i,
                    "value": val,
                    "z_score": round(z, 2),
                    "cusum_positive": round(c_pos, 2),
                    "cusum_negative": round(c_neg, 2),
                    "direction": "UPWARD_SHIFT" if c_pos > decision_h else "DOWNWARD_SHIFT"
                })
        return {"anomalies_detected": len(anomalies), "alarm_points": anomalies}

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

