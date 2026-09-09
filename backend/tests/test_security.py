"""
MedPredict AI — Cryptography & Security Tests
"""

from backend.app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    decode_token
)

def test_password_hashing():
    password = "SuperSecurePassword123!"
    hashed = get_password_hash(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("WrongPassword123!", hashed) is False

def test_jwt_access_token():
    user_id = "test-user-uuid-1234"
    claims = {"role": "DOCTOR", "email": "doctor@medpredict.ai"}
    token = create_access_token(subject=user_id, extra_claims=claims)
    assert isinstance(token, str)
    assert len(token) > 20

    decoded = decode_token(token)
    assert decoded is not None
    assert decoded["sub"] == user_id
    assert decoded["role"] == "DOCTOR"
    assert decoded["email"] == "doctor@medpredict.ai"
    assert "exp" in decoded

def test_invalid_jwt_token():
    invalid_token = "invalid.token.structure"
    decoded = decode_token(invalid_token)
    assert decoded is None
