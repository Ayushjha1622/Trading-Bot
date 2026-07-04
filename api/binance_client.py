from api.auth import BinanceAuth
from api.client import HttpClient
from api.endpoints import ACCOUNT, EXCHANGE_INFO, OPEN_ORDERS, ORDER, SERVER_TIME


class BinanceClient:
    def __init__(self):
        self.http = HttpClient()

    def get_server_time(self):
        return self.http.get(SERVER_TIME)

    def get_exchange_info(self):
        return self.http.get(EXCHANGE_INFO)

    def get_account_info(self):
        params = BinanceAuth.sign({})
        return self.http.get(
            ACCOUNT,
            params=params,
            headers=BinanceAuth.headers(),
        )

    def place_order(self, params: dict):
        signed_params = BinanceAuth.sign(params)
        return self.http.post(
            ORDER,
            data=signed_params,
            headers=BinanceAuth.headers(),
        )

    def get_order(self, symbol: str, order_id: int):
        params = BinanceAuth.sign({
            "symbol": symbol,
            "orderId": order_id,
        })
        return self.http.get(
            ORDER,
            params=params,
            headers=BinanceAuth.headers(),
        )

    def get_open_orders(self, symbol: str | None = None):
        params = BinanceAuth.sign({"symbol": symbol} if symbol else {})
        return self.http.get(
            OPEN_ORDERS,
            params=params,
            headers=BinanceAuth.headers(),
        )

    def cancel_order(self, symbol: str, order_id: int):
        params = BinanceAuth.sign({
            "symbol": symbol,
            "orderId": order_id,
        })
        return self.http.delete(
            ORDER,
            params=params,
            headers=BinanceAuth.headers(),
        )
    