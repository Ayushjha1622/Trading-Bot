from pydantic import BaseModel


class Account(BaseModel):
    total_balance: float
    available_balance: float
    total_positions: int
    total_unrealized_pnl: float


class Position(BaseModel):
    symbol: str
    quantity: float
    entry_price: float
    unrealized_pnl: float
    unrealized_pnl_percent: float
