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

    def place_order(self, order: OrderRequest):
        params = BinanceAuth.sign(order.model_dump(exclude_none=True))
        return self.http.post(
            ORDER,
            params=params,
            headers=BinanceAuth.headers(),
            json=order.model_dump(exclude_none=True),
        )