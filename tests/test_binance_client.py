from api.binance_client import BinanceClient


class DummyHttp:
    def __init__(self):
        self.calls = []

    def post(self, endpoint, **kwargs):
        self.calls.append((endpoint, kwargs))
        return {"status": "ok"}

    def delete(self, endpoint, **kwargs):
        self.calls.append((endpoint, kwargs))
        return {"status": "canceled"}


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


def test_cancel_order_uses_signed_params_and_delete_call():
    client = BinanceClient()
    client.http = DummyHttp()

    response = client.cancel_order("BTCUSDT", 123456)

    assert response == {"status": "canceled"}
    endpoint, kwargs = client.http.calls[0]
    assert endpoint == "/fapi/v1/order"
    assert "params" in kwargs
    assert "headers" in kwargs
    assert kwargs["params"]["symbol"] == "BTCUSDT"
    assert kwargs["params"]["orderId"] == 123456
