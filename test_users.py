"""
Test suite for the /users endpoints on reqres.in
Covers positive (valid input) and negative (invalid input) scenarios.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient


# ---------- POSITIVE TEST CASES ----------

def test_get_single_user_valid():
    """GET a user that exists -> should return 200 and correct data structure"""
    response = APIClient.get("/users/2")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert body["data"]["id"] == 2
    assert "email" in body["data"]


def test_get_users_list():
    """GET list of users -> should return 200 and a non-empty list"""
    response = APIClient.get("/users", params={"page": 1})
    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]) > 0


def test_create_user_valid():
    """POST a new user with valid data -> should return 201 Created"""
    payload = {"name": "Kapil Bhardwaj", "job": "QA Automation Engineer"}
    response = APIClient.post("/users", data=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body


def test_update_user_valid():
    """PUT to update an existing user -> should return 200 OK"""
    payload = {"name": "Kapil Bhardwaj", "job": "Senior QA Engineer"}
    response = APIClient.put("/users/2", data=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["job"] == "Senior QA Engineer"


def test_delete_user_valid():
    """DELETE an existing user -> should return 204 No Content"""
    response = APIClient.delete("/users/2")
    assert response.status_code == 204


# ---------- NEGATIVE TEST CASES ----------

def test_get_single_user_not_found():
    """GET a user that does NOT exist -> should return 404"""
    response = APIClient.get("/users/9999")
    assert response.status_code == 404


def test_create_user_missing_fields():
    """POST with empty payload -> API still returns 201 but response should
    not contain a valid 'job' field, since none was sent"""
    response = APIClient.post("/users", data={})
    assert response.status_code == 201
    body = response.json()
    assert body.get("job") is None


def test_get_user_invalid_id_format():
    """GET with a non-numeric ID -> should return 404, not a server error (500)"""
    response = APIClient.get("/users/abc")
    assert response.status_code == 404
