from api.auth import BinanceAuth
from api.client import HttpClient
from api.endpoints import ACCOUNT, EXCHANGE_INFO, ORDER, SERVER_TIME
from models.order import OrderRequest


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
    