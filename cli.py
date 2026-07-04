import argparse

from models.enums import OrderSide, OrderType
from models.order import OrderRequest
from services.order_service import OrderService


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side",
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type",
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity",
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT orders)",
    )

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        parser.error("--price is required for LIMIT orders.")

    return args


def main():
    args = parse_arguments()
    service = OrderService()
    order = OrderRequest(
        symbol=args.symbol.upper(),
        side=OrderSide(args.side),
        order_type=OrderType(args.type),
        quantity=args.quantity,
        price=args.price,
    )

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {order.symbol}")
    print(f"Side     : {order.side.value}")
    print(f"Type     : {order.order_type.value}")
    print(f"Quantity : {order.quantity}")
    if order.price is not None:
        print(f"Price    : {order.price}")
    print("===================================\n")

    try:
        response = service.place_order(order)
        print("========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response['orderId']}")
        print(f"Status        : {response['status']}")
        print(f"Side          : {response['side']}")
        print(f"Type          : {response['type']}")
        print(f"Executed Qty  : {response['executedQty']}")
        if response.get("avgPrice"):
            print(f"Average Price : {response['avgPrice']}")
        if response.get("price"):
            print(f"Order Price   : {response['price']}")
        print("====================================")
        print("✅ Order placed successfully.")
    except Exception as exc:
        print("\n❌ Order Failed")
        print(exc)


if __name__ == "__main__":
    main()