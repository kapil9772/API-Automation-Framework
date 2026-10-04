import requests


class APIClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, **kwargs):
        return self.session.get(self._url(endpoint), timeout=self.timeout, **kwargs)

    def post(self, endpoint, payload=None, **kwargs):
        return self.session.post(self._url(endpoint), json=payload, timeout=self.timeout, **kwargs)

    def put(self, endpoint, payload=None, **kwargs):
        return self.session.put(self._url(endpoint), json=payload, timeout=self.timeout, **kwargs)

    def patch(self, endpoint, payload=None, **kwargs):
        return self.session.patch(self._url(endpoint), json=payload, timeout=self.timeout, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self._url(endpoint), timeout=self.timeout, **kwargs)