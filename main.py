from api.binance_client import BinanceClient


def main():
    client = BinanceClient()

    exchange = client.get_exchange_info()

    print(exchange.keys())


if __name__ == "__main__":
    main()