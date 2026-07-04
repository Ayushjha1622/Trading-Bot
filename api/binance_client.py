from api.client import HttpClient
from api.endpoints import (
    SERVER_TIME,
    EXCHANGE_INFO,
)


class BinanceClient:
    def __init__(self):
        self.http = HttpClient()

    def get_server_time(self):
        return self.http.get(SERVER_TIME)

    def get_exchange_info(self):
        return self.http.get(EXCHANGE_INFO)