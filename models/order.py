from pydantic import BaseModel
from typing import Optional


class OrderRequest(BaseModel):
    symbol: str
    side: str
    type: str
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None


class OrderResponse(BaseModel):
    order_id: int
    symbol: str
    side: str
    type: str
    quantity: float
    status: str
    timestamp: int
