from .client import APIClient
from .endpoints import TIME


class BinanceClient(APIClient):
    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)

    def test_connection(self):
        return self.request("GET", TIME)
