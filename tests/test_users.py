import pytest
from utils.schema_validator import validate_schema, USER_SCHEMA


@pytest.mark.smoke
def test_get_all_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 10


@pytest.mark.smoke
def test_get_single_user(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data


@pytest.mark.regression
def test_get_user_not_found(api_client):
    response = api_client.get("/users/9999")
    assert response.status_code == 404


@pytest.mark.regression
def test_user_schema(api_client):
    response = api_client.get("/users/1")
    validate_schema(response.json(), USER_SCHEMA)


@pytest.mark.regression
@pytest.mark.parametrize("user_id", range(1, 11))
def test_all_users_have_valid_data(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id
    validate_schema(response.json(), USER_SCHEMA)


@pytest.mark.regression
def test_response_time(api_client):
    response = api_client.get("/users")
    assert response.elapsed.total_seconds() < 3