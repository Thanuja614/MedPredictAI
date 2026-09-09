"""
MedPredict AI — Role-Based Access Control (RBAC) API Tests
Verifies least privilege enforcement across PATIENT, DOCTOR, DATA_SCIENTIST, ADMIN, and AUDITOR roles.
"""

def test_rbac_patient_forbidden_from_admin_routes(client):
    # Register as PATIENT
    patient_payload = {
        "email": "normal.patient@medpredict.ai",
        "password": "Password123!",
        "first_name": "Normal",
        "last_name": "Patient",
        "role": "PATIENT"
    }
    client.post("/api/v1/auth/register", json=patient_payload)
    login_res = client.post("/api/v1/auth/login", json={
        "email": patient_payload["email"],
        "password": patient_payload["password"]
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Access own profile (should succeed)
    me_res = client.get("/api/v1/users/me", headers=headers)
    assert me_res.status_code == 200
    assert me_res.json()["email"] == patient_payload["email"]

    # Attempt to access user management (must fail with 403)
    list_res = client.get("/api/v1/users/", headers=headers)
    assert list_res.status_code == 403
    err = list_res.json()
    assert err["success"] is False
    assert err["error"]["code"] == "FORBIDDEN"

def test_rbac_admin_permitted_on_governance_routes(client):
    # Register as ADMIN
    admin_payload = {
        "email": "super.admin@medpredict.ai",
        "password": "AdminPassword123!",
        "first_name": "Super",
        "last_name": "Admin",
        "role": "ADMIN"
    }
    client.post("/api/v1/auth/register", json=admin_payload)
    login_res = client.post("/api/v1/auth/login", json={
        "email": admin_payload["email"],
        "password": admin_payload["password"]
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Access user management (should succeed with 200)
    list_res = client.get("/api/v1/users/", headers=headers)
    assert list_res.status_code == 200
    users = list_res.json()
    assert len(users) >= 1
