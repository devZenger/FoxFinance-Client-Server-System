from pydantic import BaseModel, field_validator

from utilities import check_fin_amount, check_isin


class BankTransfer(BaseModel):
    fin_amount: float
    transfer_type: str
    usage: str | None = None

    @field_validator("fin_amount")
    @classmethod
    def validate_fin_amount(cls, v):
        return check_fin_amount(v)

    @field_validator("transfer_type")
    @classmethod
    def validate_transfer_type(cls, v):
        if v == "withdraw" or v == "deposit":
            return v
        else:
            raise ValueError("Transfertyp stimmt nicht")


class StockTrade(BaseModel):
    isin: str
    amount: int
    transaction_type: str

    @field_validator("isin")
    @classmethod
    def validate_isin(cls, v):
        return check_isin(v)

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v):
        if v > 1:
            return v
        else:
            raise ValueError("Anzahl muss größer 0 sein.")

    @field_validator("transaction_type")
    @classmethod
    def validate_transaction_type(cls, v):
        if v == "buy" or v == "sell":
            return v
        else:
            raise ValueError("Transaktionstyp stimmt nicht")


class WatchlistOrder(BaseModel):
    isin: str

    @field_validator("isin")
    @classmethod
    def validate_isin(cls, v):
        return check_isin(v)
