from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel


from service import User, get_current_active_user, search_stock, start_stock_transaction

router = APIRouter()

class User(BaseModel):
    #username: str
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None


class StockTrade(BaseModel):
    isin: str
    amount: int
    transaction_type: str


@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term: str, current_customer: Annotated[User, Depends(get_current_active_user)]):

    result = search_stock(search_term)     
    return {"message":result}


@router.post("/depot/tradestocks/")
async def trade_stocks(stock_trade: StockTrade, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:

        start_stock_transaction(current_customer["customer_id"], stock_trade)

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
