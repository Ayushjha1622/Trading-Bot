from typing import Optional

from pydantic import BaseModel, Field, model_validator

from models.enums import (
    OrderSide,
    OrderType,
    TimeInForce,
)


class OrderRequest(BaseModel):

    symbol: str

    side: OrderSide

    order_type: OrderType

    quantity: float = Field(gt=0)

    price: Optional[float] = None

    time_in_force: TimeInForce = TimeInForce.GTC

    @model_validator(mode="after")
    def validate_order(self):

        if self.order_type == OrderType.LIMIT and self.price is None:
            raise ValueError(
                "Price is required for LIMIT orders."
            )

        if self.order_type == OrderType.MARKET and self.price is not None:
            raise ValueError(
                "Price should not be provided for MARKET orders."
            )

        return self