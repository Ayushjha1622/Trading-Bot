from .client import HttpClient
from .endpoints import TIME


class BinanceClient(HttpClient):
    def __init__(self, base_url: str):
        super().__init__()
        self.client.base_url = base_url

    def test_connection(self):
        return self.get(TIME)
