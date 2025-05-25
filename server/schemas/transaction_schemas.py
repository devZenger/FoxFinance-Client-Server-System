from pydantic import BaseModel


class BankTransfer(BaseModel):
    fin_amount: float
    transfer_type: str
    usage: str | None = None


class StockTrade(BaseModel):
    isin: str
    amount: int
    transaction_type: str


class WatchlistOrder(BaseModel):
    isin: str
    transaction_type: bool