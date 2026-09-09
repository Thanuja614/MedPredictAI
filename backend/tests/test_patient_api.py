"""
MedPredict AI — Patient & Clinical Domain API Tests
"""

from datetime import date
from backend.app.models.disease import Disease

def test_patient_workflow(client, db_session):
    # Register patient user
    reg = {
        "email": "clinical.flow@medpredict.ai",
        "password": "Password123!",
        "first_name": "Clinical",
        "last_name": "Patient",
        "role": "PATIENT"
    }
    client.post("/api/v1/auth/register", json=reg)
    login_res = client.post("/api/v1/auth/login", json={"email": reg["email"], "password": reg["password"]})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get my patient profile
    me_res = client.get("/api/v1/patients/me", headers=headers)
    assert me_res.status_code == 200
    patient_data = me_res.json()
    patient_id = patient_data["id"]

    # Update patient demographics
    update_res = client.put(f"/api/v1/patients/{patient_id}", json={
        "blood_group": "B+",
        "emergency_contact": "Guardian (555-9988)"
    }, headers=headers)
    assert update_res.status_code == 200
    assert update_res.json()["blood_group"] == "B+"

    # Update medical profile
    med_res = client.put(f"/api/v1/patients/{patient_id}/medical-profile", json={
        "allergies": "Aspirin, Sulfa drugs",
        "chronic_conditions": "Asthma",
        "lifestyle_notes": "Non-smoker, moderate alcohol"
    }, headers=headers)
    assert med_res.status_code == 200
    assert "Aspirin" in med_res.json()["allergies"]

    # Create Disease for assessment
    disease = Disease(name="Test Chronic Kidney", slug="test_ckd", category="Nephrology")
    db_session.add(disease)
    db_session.commit()

    # Create assessment
    assess_res = client.post(f"/api/v1/patients/{patient_id}/assessments", json={
        "disease_id": disease.id,
        "notes": "Routine renal panel screening requested"
    }, headers=headers)
    assert assess_res.status_code == 201
    assert assess_res.json()["disease_id"] == disease.id

    # List assessments
    list_assess = client.get(f"/api/v1/patients/{patient_id}/assessments", headers=headers)
    assert list_assess.status_code == 200
    assert len(list_assess.json()) == 1
