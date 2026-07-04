from api.binance_client import BinanceClient

client = BinanceClient()

response = client.get_order(
    "BTCUSDT",
    18969988068
)

print(response)