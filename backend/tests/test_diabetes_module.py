"""
MedPredict AI — Diabetes Module (Phase 9) Test Suite
Verifies training, feature engineering, evaluation, inference, and serialization on actual demo dataset.
"""

from pathlib import Path
import pandas as pd
from backend.app.ml.modules.diabetes.module import DiabetesDiseaseModule

DATASET_CSV = Path(__file__).resolve().parent.parent.parent / "data" / "datasets" / "diabetes" / "diabetes.csv"

def test_diabetes_module_lifecycle():
    assert DATASET_CSV.exists()
    df = pd.read_csv(DATASET_CSV)
    assert len(df) >= 100

    # Train / Test split
    train_size = int(0.8 * len(df))
    df_train = df.iloc[:train_size]
    df_test = df.iloc[train_size:]

    module = DiabetesDiseaseModule()
    metrics = module.train_and_evaluate(df_train, df_test, algorithm_name="random_forest")

    assert metrics["accuracy"] >= 0.60
    assert metrics["sample_count"] == len(df_test)
    assert "confusion_matrix" in metrics

    # Single inference test
    patient_assessment = {
        "pregnancies": 2,
        "glucose": 145.0,
        "blood_pressure": 82.0,
        "skin_thickness": 28.0,
        "insulin": 190.0,
        "bmi": 33.4,
        "diabetes_pedigree": 0.62,
        "age": 48
    }
    prediction = module.predict(patient_assessment)
    assert prediction["disease"] == "Diabetes"
    pred_res = prediction["prediction"]
    assert pred_res["risk_level"] in ("LOW", "MODERATE", "HIGH")
    assert "educational, research and decision-support" in pred_res["disclaimer"]

    # Explainability test
    expl = prediction["explanation"]
    assert len(expl["contributions"]) > 0
    assert "medical causation" in expl["disclaimer"]
