from models.order import OrderRequest
from models.enums import (
    OrderSide,
    OrderType,
)


def main():

    order = OrderRequest(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=0.001,
    )

    print(order.model_dump())


if __name__ == "__main__":
    main()