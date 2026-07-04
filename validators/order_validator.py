from models.order import OrderRequest
from models.enums import OrderType


class OrderValidator:

    @staticmethod
    def validate(order: OrderRequest):

        if order.quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        if (
            order.order_type == OrderType.LIMIT
            and order.price is None
        ):
            raise ValueError(
                "LIMIT order requires a price."
            )

        if (
            order.order_type == OrderType.MARKET
            and order.price is not None
        ):
            raise ValueError(
                "MARKET order should not include a price."
            )

        return True