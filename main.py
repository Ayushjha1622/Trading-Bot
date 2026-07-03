from api.binance import BinanceClient
from config import settings


def main():
    client = BinanceClient(settings.base_url)

    data = client.test_connection()

    print("✅ Connected Successfully")
    print(data)


if __name__ == "__main__":
    main()