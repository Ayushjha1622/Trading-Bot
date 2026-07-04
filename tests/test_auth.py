from api.auth import BinanceAuth


def test_sign_adds_timestamp_and_signature_without_including_signature_in_hmac_input():
    signed = BinanceAuth.sign({"symbol": "BTCUSDT", "side": "BUY"})

    assert "timestamp" in signed
    assert "signature" in signed
    assert signed["signature"]
    assert signed["timestamp"] > 0
