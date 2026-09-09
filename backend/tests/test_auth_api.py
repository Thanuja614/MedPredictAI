"""
MedPredict AI — Authentication Endpoints Test Suite
"""

def test_register_user(client):
    payload = {
        "email": "new.patient@medpredict.ai",
        "password": "Password123!",
        "first_name": "Alice",
        "last_name": "Wonderland",
        "role": "PATIENT"
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "new.patient@medpredict.ai"
    assert data["first_name"] == "Alice"
    assert len(data["roles"]) == 1
    assert data["roles"][0]["name"] == "PATIENT"

def test_register_duplicate_email_fails(client):
    payload = {
        "email": "duplicate@medpredict.ai",
        "password": "Password123!",
        "first_name": "Bob",
        "last_name": "Builder"
    }
    res1 = client.post("/api/v1/auth/register", json=payload)
    assert res1.status_code == 201

    res2 = client.post("/api/v1/auth/register", json=payload)
    assert res2.status_code == 422
    err = res2.json()
    assert err["success"] is False
    assert "already exists" in err["error"]["message"]

def test_login_flow(client):
    # Register
    reg_payload = {
        "email": "login.test@medpredict.ai",
        "password": "CorrectPassword123!",
        "first_name": "Charlie",
        "last_name": "Brown"
    }
    client.post("/api/v1/auth/register", json=reg_payload)

    # Valid Login
    login_payload = {
        "email": "login.test@medpredict.ai",
        "password": "CorrectPassword123!"
    }
    res = client.post("/api/v1/auth/login", json=login_payload)
    assert res.status_code == 200
    token_data = res.json()
    assert "access_token" in token_data
    assert "refresh_token" in token_data
    assert token_data["token_type"] == "bearer"

    # Invalid Login
    bad_login = {
        "email": "login.test@medpredict.ai",
        "password": "WrongPassword!"
    }
    bad_res = client.post("/api/v1/auth/login", json=bad_login)
    assert bad_res.status_code == 401

def test_refresh_token_flow(client):
    reg = {
        "email": "refresh.test@medpredict.ai",
        "password": "Password123!",
        "first_name": "Dan",
        "last_name": "Evans"
    }
    client.post("/api/v1/auth/register", json=reg)

    login_res = client.post("/api/v1/auth/login", json={"email": reg["email"], "password": reg["password"]})
    tokens = login_res.json()

    refresh_res = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert refresh_res.status_code == 200
    new_tokens = refresh_res.json()
    assert "access_token" in new_tokens
    assert new_tokens["access_token"] != tokens["access_token"]

def test_password_reset_flow(client):
    reg = {
        "email": "reset.test@medpredict.ai",
        "password": "OldPassword123!",
        "first_name": "Eve",
        "last_name": "Smith"
    }
    client.post("/api/v1/auth/register", json=reg)

    # Request reset
    req_res = client.post("/api/v1/auth/password-reset/request", json={"email": reg["email"]})
    assert req_res.status_code == 200
    reset_token = req_res.json()["reset_token"]

    # Confirm reset
    conf_res = client.post("/api/v1/auth/password-reset/confirm", json={
        "token": reset_token,
        "new_password": "BrandNewPassword123!"
    })
    assert conf_res.status_code == 200

    # Login with new password
    login_new = client.post("/api/v1/auth/login", json={
        "email": reg["email"],
        "password": "BrandNewPassword123!"
    })
    assert login_new.status_code == 200
