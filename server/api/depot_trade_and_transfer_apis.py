from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from utilities import error_msg_no_service, exceptions_handler, check_not_None_and_empty
from service import (get_current_active_user,
                     get_customer_balance,
                     do_past_fin_transactions,
                     make_bank_transfer,
                     start_stock_transaction,
                     past_transactions)
from schemas import User, BankTransfer, StockTrade

router = APIRouter()


# APIs who ether bank transfer or stock transaction are.
# financial related:
# 1. get("/depot/current_balance/")
# 2. get("/depot/pastfinancialtransactions/{search_start}/{search_end}")
# 3. post("/depot/banktransfer/")
#
# stock trade related:
# 4. get("/depot/pasttransactions/{search_start}/{search_end}")
# 5. post("/depot/tradestocks/")


# 1. get("/depot/current_balance/")
@router.get("/depot/current_balance/")
async def get_current_balance(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        current_balance = get_customer_balance(current_customer["customer_id"])
        return {"message": current_balance}

    except Exception as e:
        exceptions_handler(e, "get_current_balance() (depot_financial_apis.py)")


# 2. get("/depot/pastfinancialtransactions/{search_start}/{search_end}")
@router.get("/depot/pastfinancialtransactions/{search_start}/{search_end}")
async def get_past_financial_transactions(search_start: str,
                                          search_end: str,
                                          current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        check_not_None_and_empty(search_start)
        check_not_None_and_empty(search_end)

        succes, transactions = do_past_fin_transactions(current_customer["customer_id"], search_start, search_end)
        if succes:
            return {"message": transactions}
        else:
            raise HTTPException(status_code=422, detail=error_msg_no_service)

    except Exception as e:
        exceptions_handler(e, "get_past_financial_transactions() (depot_financial_apis.py)")


# 3. post("/depot/banktransfer/")
@router.post("/depot/banktransfer/")
async def post_bank_transfer(bank_transfer: BankTransfer,
                             current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        to_transfer = bank_transfer.model_dump()
        transfer = make_bank_transfer(current_customer["customer_id"], to_transfer)
        return {"message": transfer}

    except Exception as e:
        exceptions_handler(e, "post_bank_transfer() (depot_financial_apis.py)")


# 4 get("/depot/pasttransactions/{search_start}/{search_end}")
@router.get("/depot/pasttransactions/{search_start}/{search_end}")
async def get_past_transactions(search_start: str,
                                search_end: str,
                                current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        check_not_None_and_empty(search_start)
        check_not_None_and_empty(search_end)

        transactions = past_transactions(current_customer["customer_id"], search_start, search_end)
        return {"message": transactions}

    except Exception as e:
        exceptions_handler(e, "get_past_transactions() (dept_overview_apis.py)")


# 5 post("/depot/tradestocks/")
@router.post("/depot/tradestocks/")
async def trade_stocks(stock_trade: StockTrade, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        to_trade = stock_trade.model_dump()
        message = start_stock_transaction(current_customer["customer_id"], to_trade)

        return {"message": message}

    except Exception as e:
        exceptions_handler(e, "trade_stocks() (depot_stock_api.py)")
