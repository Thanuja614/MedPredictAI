"""
MedPredict AI — Heart Disease Module (Phase 10) Test Suite
"""

from pathlib import Path
import pandas as pd
from backend.app.ml.modules.heart.module import HeartDiseaseModule

DATASET_CSV = Path(__file__).resolve().parent.parent.parent / "data" / "datasets" / "heart" / "heart.csv"

def test_heart_module_lifecycle():
    assert DATASET_CSV.exists()
    df = pd.read_csv(DATASET_CSV)
    assert len(df) >= 100

    train_size = int(0.8 * len(df))
    df_train = df.iloc[:train_size]
    df_test = df.iloc[train_size:]

    module = HeartDiseaseModule()
    metrics = module.train_and_evaluate(df_train, df_test, algorithm_name="random_forest")

    assert metrics["accuracy"] >= 0.55
    assert metrics["sample_count"] == len(df_test)
    assert "roc_auc" in metrics

    patient_assessment = {
        "age": 62,
        "sex": 1,
        "chest_pain_type": 2,
        "resting_bp": 142.0,
        "cholesterol": 268.0,
        "fasting_blood_sugar": 0,
        "resting_ecg": 1,
        "max_hr": 145.0,
        "exercise_angina": 1,
        "st_depression": 1.8,
        "st_slope": 1
    }
    prediction = module.predict(patient_assessment)
    assert prediction["disease"] == "Heart Disease"
    pred_res = prediction["prediction"]
    assert pred_res["risk_level"] in ("LOW", "MODERATE", "HIGH")
    assert "educational, research and decision-support" in pred_res["disclaimer"]
