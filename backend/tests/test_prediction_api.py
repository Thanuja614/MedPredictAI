"""
MedPredict AI — Predictions, Diseases & Inference API Test Suite
"""

from backend.app.ml.framework.base_predictor import MEDICAL_SAFETY_DISCLAIMER

def test_disease_catalog_endpoints(client):
    # List all diseases
    res = client.get("/api/v1/diseases/")
    assert res.status_code == 200
    diseases = res.json()
    assert len(diseases) == 10
    slugs = [d["slug"] for d in diseases]
    assert "diabetes" in slugs
    assert "heart" in slugs
    assert "parkinsons" in slugs

    # Get single disease details
    d_res = client.get("/api/v1/diseases/diabetes")
    assert d_res.status_code == 200
    data = d_res.json()
    assert data["slug"] == "diabetes"
    assert len(data["features"]) == 8
    assert "glucose" in [f["name"] for f in data["features"]]

    # Test symptom match
    symp_res = client.post("/api/v1/diseases/symptom-match", json={
        "symptoms": ["excessive_thirst", "frequent_urination"]
    })
    assert symp_res.status_code == 200
    matched = symp_res.json()
    matched_slugs = [m["slug"] for m in matched["matched_diseases"]]
    assert "diabetes" in matched_slugs
    assert "not constitute a clinical diagnosis" in matched["disclaimer"]

def test_prediction_evaluation_api_flow(client):
    # Register and authenticate patient
    reg = {
        "email": "predict.patient@medpredict.ai",
        "password": "Password123!",
        "first_name": "Eval",
        "last_name": "Patient",
        "role": "PATIENT"
    }
    client.post("/api/v1/auth/register", json=reg)
    login_res = client.post("/api/v1/auth/login", json={"email": reg["email"], "password": reg["password"]})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Evaluate diabetes prediction
    eval_payload = {
        "disease_slug": "diabetes",
        "features": {
            "pregnancies": 3,
            "glucose": 155.0,
            "blood_pressure": 85.0,
            "skin_thickness": 32.0,
            "insulin": 210.0,
            "bmi": 36.2,
            "diabetes_pedigree": 0.72,
            "age": 52
        }
    }
    pred_res = client.post("/api/v1/predictions/evaluate", json=eval_payload, headers=headers)
    assert pred_res.status_code == 200
    result = pred_res.json()

    assert result["disease_slug"] == "diabetes"
    assert "probability" in result
    assert result["risk_level"] in ("LOW", "MODERATE", "HIGH")
    assert result["disclaimer"] == MEDICAL_SAFETY_DISCLAIMER

    # Validate explanation
    expl = result["explanation"]
    assert "contributions" in expl
    assert len(expl["contributions"]) > 0

    pred_id = result["prediction_id"]

    # Retrieve prediction detail
    detail_res = client.get(f"/api/v1/predictions/{pred_id}", headers=headers)
    assert detail_res.status_code == 200
    detail = detail_res.json()
    assert detail["id"] == pred_id
    assert detail["inputs"]["glucose"] == 155.0
    assert len(detail["explanation"]["contributions"]) > 0
