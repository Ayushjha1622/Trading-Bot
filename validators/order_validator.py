from models.order import OrderRequest
from typing import Dict, Any


def validate_order(payload: Dict[str, Any]) -> OrderRequest:
    order = OrderRequest(**payload)

    if order.side not in {"BUY", "SELL"}:
        raise ValueError("side must be BUY or SELL")

    if order.type not in {"MARKET", "LIMIT", "STOP_LOSS", "TAKE_PROFIT"}:
        raise ValueError("type is not supported")

    return order
