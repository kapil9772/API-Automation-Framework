import pytest
from utils.schema_validator import validate_schema, POST_SCHEMA


@pytest.mark.smoke
def test_get_all_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100


@pytest.mark.smoke
def test_get_single_post_schema(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    validate_schema(response.json(), POST_SCHEMA)


@pytest.mark.regression
def test_filter_posts_by_user(api_client):
    response = api_client.get("/posts", params={"userId": 1})
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 10
    assert all(post["userId"] == 1 for post in posts)


@pytest.mark.regression
def test_get_post_comments(api_client):
    response = api_client.get("/posts/1/comments")
    assert response.status_code == 200
    assert len(response.json()) == 5


@pytest.mark.smoke
def test_create_post(api_client):
    payload = {"title": "QA Automation", "body": "Testing with Python", "userId": 1}
    response = api_client.post("/posts", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == 1
    assert "id" in data


@pytest.mark.regression
def test_update_post_put(api_client):
    payload = {"id": 1, "title": "Updated", "body": "Updated body", "userId": 1}
    response = api_client.put("/posts/1", payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


@pytest.mark.regression
def test_update_post_patch(api_client):
    response = api_client.patch("/posts/1", {"title": "Patched title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Patched title"


@pytest.mark.regression
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200


@pytest.mark.regression
def test_post_not_found(api_client):
    response = api_client.get("/posts/9999")
    assert response.status_code == 404