"""
Test suite for the /login endpoint on reqres.in
Covers valid login, missing password, and invalid credentials.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient


def test_login_valid_credentials():
    """Valid email + password -> should return 200 and a token"""
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = APIClient.post("/login", data=payload)
    assert response.status_code == 200
    body = response.json()
    assert "token" in body


def test_login_missing_password():
    """Email given but password missing -> should return 400 Bad Request"""
    payload = {"email": "eve.holt@reqres.in"}
    response = APIClient.post("/login", data=payload)
    assert response.status_code == 400
    body = response.json()
    assert "error" in body


def test_login_invalid_user():
    """Non-existent user -> should return 400 Bad Request, not 200"""
    payload = {"email": "not_a_real_user@reqres.in", "password": "whatever123"}
    response = APIClient.post("/login", data=payload)
    assert response.status_code == 400
