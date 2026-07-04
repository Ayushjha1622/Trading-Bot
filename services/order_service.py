from api.binance_client import BinanceClient
from models.order import OrderRequest, OrderResponse


class OrderService:
    def __init__(self, client: BinanceClient):
        self.client = client

    def place_order(self, order: OrderRequest) -> OrderResponse:
        data = self.client.request(
            "POST",
            "/fapi/v1/order",
            json=order.model_dump(exclude_none=True),
        )
        return OrderResponse(**data)
