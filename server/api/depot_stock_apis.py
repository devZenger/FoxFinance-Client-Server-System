from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from utilitys import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import (get_current_active_user,
                     search_stock,
                     start_stock_transaction,
                     load_watchlist,
                     editing_watchlist)
from schemas import User, StockTrade, WatchlistOrder

router = APIRouter()


@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term: str, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        result = search_stock(search_term)
        return {"message": result}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.post("/depot/tradestocks/")
async def trade_stocks(stock_trade: StockTrade, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        start_stock_transaction(current_customer["customer_id"], stock_trade)

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.get("/depot/watchlist/")
async def get_watchlist(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        result = load_watchlist(current_customer["customer_id"])
        return {"message": result}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.post("/depot/editingwatchlist/")
async def post_editing_watchlist(watchlist_order: WatchlistOrder,
                                 current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        editing_watchlist(current_customer["customer_id"], watchlist_order)

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
