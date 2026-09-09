"""
Unit tests for MedPredict AI Clinical Decision Support & Ontologies.
"""

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_icd10_search():
    res = client.get("/api/v1/clinical/icd10/search?q=hypertension")
    assert res.status_code == 200
    data = res.json()
    assert data["count"] >= 1
    assert any("hypertension" in r["title"].lower() for r in data["results"])

def test_loinc_search():
    res = client.get("/api/v1/clinical/loinc/search?q=glucose")
    assert res.status_code == 200
    data = res.json()
    assert data["count"] >= 1

def test_biomarker_eval_normal():
    res = client.post("/api/v1/clinical/biomarker/evaluate", json={
        "loinc_code": "1558-6",
        "value": 85.0,
        "unit": "mg/dL",
        "gender": "male",
        "age": 45
    })
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "NORMAL"
    assert data["is_critical_panic"] is False

def test_biomarker_eval_panic_high():
    res = client.post("/api/v1/clinical/biomarker/evaluate", json={
        "loinc_code": "1558-6",
        "value": 500.0,
        "unit": "mg/dL",
        "gender": "male",
        "age": 45
    })
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "CRITICAL_HIGH"
    assert data["is_critical_panic"] is True

def test_drug_interaction_screening():
    res = client.post("/api/v1/clinical/medications/screen-interactions", json={
        "medications": ["Apixaban", "Clopidogrel", "Amiodarone"]
    })
    assert res.status_code == 200
    data = res.json()
    assert data["total_medications"] == 3
    assert data["interactions_found"] >= 1

def test_ascvd_risk_protocol():
    res = client.post("/api/v1/clinical/protocols/ascvd-10year", json={
        "age": 55,
        "gender": "male",
        "race": "white",
        "total_cholesterol": 210,
        "hdl_cholesterol": 45,
        "systolic_bp": 140,
        "bp_treated": True,
        "smoker": False,
        "diabetes": False
    })
    assert res.status_code == 200
    data = res.json()
    assert data["risk_percentage"] > 0.0
    assert data["risk_category"] in ("LOW", "BORDERLINE", "INTERMEDIATE", "HIGH")
    assert len(data["guideline_recommendations"]) > 0
