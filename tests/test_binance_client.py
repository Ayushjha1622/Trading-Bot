from api.binance_client import BinanceClient


class DummyHttp:
    def __init__(self):
        self.calls = []

    def post(self, endpoint, **kwargs):
        self.calls.append((endpoint, kwargs))
        return {"status": "ok"}


def test_place_order_uses_form_body_for_signed_params():
    client = BinanceClient()
    client.http = DummyHttp()

    response = client.place_order(
        {
            "symbol": "BTCUSDT",
            "side": "BUY",
            "type": "MARKET",
            "quantity": 0.001,
        }
    )

    assert response == {"status": "ok"}
    endpoint, kwargs = client.http.calls[0]
    assert endpoint == "/fapi/v1/order"
    assert "data" in kwargs
    assert "params" not in kwargs
    assert "timestamp" in kwargs["data"]
