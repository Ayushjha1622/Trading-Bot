from httpx import Client
from typing import Any


class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.client = Client(base_url=base_url, timeout=timeout)

    def request(self, method: str, path: str, **kwargs: Any):
        response = self.client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()
