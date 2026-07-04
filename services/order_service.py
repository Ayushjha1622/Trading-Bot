from api.binance_client import BinanceClient
from models.enums import OrderType
from models.order import OrderRequest
from validators.order_validator import OrderValidator


class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, order: OrderRequest):
        OrderValidator.validate(order)

        payload = {
            "symbol": order.symbol,
            "side": order.side.value,
            "type": order.order_type.value,
            "quantity": order.quantity,
        }

        if order.order_type == OrderType.LIMIT:
            payload["price"] = order.price
            payload["timeInForce"] = order.time_in_force.value

        return self.client.place_order(payload)