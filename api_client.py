"""
Simple reusable API client used across all test files.
Wraps the 'requests' library so tests don't repeat the same request logic.
"""

import requests

BASE_URL = "https://reqres.in/api"

# reqres.in requires this header on their free tier
HEADERS = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}


class APIClient:

    @staticmethod
    def get(endpoint, params=None):
        return requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS, params=params)

    @staticmethod
    def post(endpoint, data=None):
        return requests.post(f"{BASE_URL}{endpoint}", headers=HEADERS, json=data)

    @staticmethod
    def put(endpoint, data=None):
        return requests.put(f"{BASE_URL}{endpoint}", headers=HEADERS, json=data)

    @staticmethod
    def delete(endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
