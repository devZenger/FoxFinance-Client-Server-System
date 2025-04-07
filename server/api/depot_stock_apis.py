from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel


from service import (User,
                     get_current_active_user,
                     search_stock,
                     start_stock_transaction,
                     load_watchlist,
                     editing_watchlist)

router = APIRouter()


# class User(BaseModel):
#    email: str
#    customer_id: int | None = None
#    disabled: bool | None = None

class StockTrade(BaseModel):
    isin: str
    amount: int
    transaction_type: str


class WatchlistOrder(BaseModel):
    isin: str
    transaction_type: bool


@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term: str,
                           current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        result = search_stock(search_term)     
        return {"message": result}

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.post("/depot/tradestocks/")
async def trade_stocks(stock_trade: StockTrade, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        start_stock_transaction(current_customer["customer_id"], stock_trade)

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/depot/watchlist/")
async def get_watchlist(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        result = load_watchlist(current_customer["customer_id"])
        return {"message": result}
        
    except Exception as e:
        print(f"\nFehler bei get_watchlist. Error: {e}\n")
        raise HTTPException(status_code=422, detail=str(e))


@router.post("/depot/editingwatchlist/")
async def post_editing_watchlist(watchlist_order: WatchlistOrder,
                                 current_customer: Annotated[User, Depends(get_current_active_user)]):

    print("start watschlist api")

    try:
        editing_watchlist(current_customer["customer_id"], watchlist_order)

    except Exception as e:
        print(f"\nFehler bei post_editing_watchlist. Error: {e}\n")
        raise HTTPException(status_code=422, detail=str(e))
