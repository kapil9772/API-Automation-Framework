import pytest
from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"
AUTH_URL = "https://httpbin.org"


@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_client():
    return APIClient(AUTH_URL)