"""
MedPredict AI — Health and Root Endpoint Tests
"""

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "MedPredict AI"
    assert "disclaimer" in data
    assert "not medical diagnoses" in data["disclaimer"]

def test_liveness_check(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "timestamp" in data

def test_readiness_check(client):
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ("ready", "degraded")
    assert "components" in data
    assert "disclaimer_enforced" in data
    assert data["disclaimer_enforced"] is True
