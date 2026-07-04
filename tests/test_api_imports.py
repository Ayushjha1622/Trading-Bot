from api.binance_client import BinanceClient
from api.client import HttpClient


def test_binance_client_uses_http_client_base_class():
    client = BinanceClient(base_url="https://example.com")

    assert isinstance(client, HttpClient)
