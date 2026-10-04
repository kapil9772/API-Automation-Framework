import pytest


@pytest.mark.smoke
def test_basic_auth_success(auth_client):
    response = auth_client.get("/basic-auth/kapil/pass123", auth=("kapil", "pass123"))
    assert response.status_code == 200
    assert response.json()["authenticated"] is True


@pytest.mark.regression
def test_basic_auth_wrong_password(auth_client):
    response = auth_client.get("/basic-auth/kapil/pass123", auth=("kapil", "wrong"))
    assert response.status_code == 401


@pytest.mark.regression
def test_basic_auth_no_credentials(auth_client):
    response = auth_client.get("/basic-auth/kapil/pass123")
    assert response.status_code == 401


@pytest.mark.smoke
def test_bearer_token_success(auth_client):
    headers = {"Authorization": "Bearer my-secret-token"}
    response = auth_client.get("/bearer", headers=headers)
    assert response.status_code == 200
    assert response.json()["token"] == "my-secret-token"


@pytest.mark.regression
def test_bearer_token_missing(auth_client):
    response = auth_client.get("/bearer")
    assert response.status_code == 401