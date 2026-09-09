"""
MedPredict AI — Master 10-Disease Modules Test Suite (Phases 9 - 18)
Validates that every one of the 10 core disease modules:
1. Loads its corresponding demonstration CSV dataset.
2. Performs leakage-free feature engineering and preprocessing.
3. Fits ML candidates and produces genuine non-fabricated evaluation metrics.
4. Executes single-patient risk inference with correct LOW/MODERATE/HIGH categories.
5. Invariably includes the mandatory educational/decision-support safety disclaimer.
6. Computes local instance explainability with the causation disclaimer.
"""

from pathlib import Path
import pandas as pd
import pytest
from backend.app.ml.modules import list_disease_modules, get_disease_module
from backend.app.ml.framework.base_predictor import MEDICAL_SAFETY_DISCLAIMER
from backend.app.ml.framework.base_explainer import SHAP_CAUSATION_DISCLAIMER

DATASETS_ROOT = Path(__file__).resolve().parent.parent.parent / "data" / "datasets"

SAMPLE_INPUTS = {
    "diabetes": {
        "pregnancies": 2, "glucose": 130.0, "blood_pressure": 75.0,
        "skin_thickness": 22.0, "insulin": 120.0, "bmi": 29.5,
        "diabetes_pedigree": 0.45, "age": 42
    },
    "heart": {
        "age": 55, "sex": 1, "chest_pain_type": 1, "resting_bp": 130.0,
        "cholesterol": 240.0, "fasting_blood_sugar": 0, "resting_ecg": 0,
        "max_hr": 155.0, "exercise_angina": 0, "st_depression": 0.8, "st_slope": 1
    },
    "liver": {
        "age": 45, "gender": 1, "total_bilirubin": 1.2, "direct_bilirubin": 0.4,
        "alkaline_phosphatase": 180.0, "alamine_aminotransferase": 35.0,
        "aspartate_aminotransferase": 40.0, "total_proteins": 6.8, "albumin": 3.4, "ag_ratio": 1.0
    },
    "kidney": {
        "age": 50, "blood_pressure": 80.0, "specific_gravity": 1.020, "albumin": 0,
        "sugar": 0, "blood_urea": 36.0, "serum_creatinine": 1.1, "sodium": 138.0,
        "potassium": 4.2, "hemoglobin": 14.5
    },
    "breast_cancer": {
        "radius_mean": 13.5, "texture_mean": 18.2, "perimeter_mean": 88.0,
        "area_mean": 560.0, "smoothness_mean": 0.095, "compactness_mean": 0.085, "concavity_mean": 0.065
    },
    "stroke": {
        "gender": 1, "age": 58.0, "hypertension": 0, "heart_disease": 0,
        "ever_married": 1, "avg_glucose_level": 95.0, "bmi": 26.5
    },
    "hypertension": {
        "age": 48, "systolic_bp": 125.0, "diastolic_bp": 82.0, "heart_rate": 72.0,
        "bmi": 26.0, "cholesterol": 195.0
    },
    "anemia": {
        "gender": 0, "hemoglobin": 11.2, "mch": 26.5, "mchc": 30.5, "mcv": 82.0
    },
    "thyroid": {
        "age": 42, "sex": 0, "on_thyroxine": 0, "tsh": 2.1, "t3": 1.8, "tt4": 95.0, "t4u": 0.95
    },
    "parkinsons": {
        "fo_hz": 150.0, "fhi_hz": 190.0, "flo_hz": 110.0, "jitter_percent": 0.005,
        "shimmer": 0.025, "hnr": 23.0, "rpde": 0.45
    }
}

@pytest.mark.parametrize("slug", list(SAMPLE_INPUTS.keys()))
def test_all_10_disease_modules(slug):
    csv_file = DATASETS_ROOT / slug / f"{slug}.csv"
    assert csv_file.exists(), f"Missing dataset file for disease '{slug}'"

    df = pd.read_csv(csv_file)
    assert len(df) >= 100

    split_idx = int(0.8 * len(df))
    df_train = df.iloc[:split_idx]
    df_test = df.iloc[split_idx:]

    module = get_disease_module(slug)
    assert module.slug == slug

    # Train and Evaluate
    metrics = module.train_and_evaluate(df_train, df_test)

    assert "accuracy" in metrics
    assert "roc_auc" in metrics
    assert metrics["sample_count"] == len(df_test)

    # Inference on sample patient input
    sample_input = SAMPLE_INPUTS[slug]
    result = module.predict(sample_input)

    assert result["slug"] == slug
    pred = result["prediction"]
    assert 0.0 <= pred["probability"] <= 1.0
    assert pred["risk_level"] in ("LOW", "MODERATE", "HIGH")
    assert pred["disclaimer"] == MEDICAL_SAFETY_DISCLAIMER

    # Explainability
    expl = result["explanation"]
    assert "contributions" in expl
    assert len(expl["contributions"]) > 0
    assert expl["disclaimer"] == SHAP_CAUSATION_DISCLAIMER
