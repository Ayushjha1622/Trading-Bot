from api.binance_client import BinanceClient


def test_binance_client_creates_http_client():
    client = BinanceClient()

    assert client.http is not None
