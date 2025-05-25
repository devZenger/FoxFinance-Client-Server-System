from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from utilities import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import (get_current_active_user,
                     get_customer_balance,
                     do_past_fin_transactions,
                     make_bank_transfer)
from schemas import User, BankTransfer

router = APIRouter()


@router.get("/depot/current_balance/")
async def get_current_balance(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        current_balance = get_customer_balance(current_customer["customer_id"])
        return {"message": current_balance}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.get("/depot/pastfinancialtransactions/{search_start}/{search_end}")
async def get_past_financial_transactions(search_start: str,
                                          search_end: str,
                                          current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        succes, transactions = do_past_fin_transactions(current_customer["customer_id"], search_start, search_end)
        if succes:
            return {"message": transactions}
        else:
            raise HTTPException(status_code=422, detail=error_msg_no_service)

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.post("/depot/banktransfer/")
async def post_bank_transfer(bank_transfer: BankTransfer,
                             current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        transfer = make_bank_transfer(current_customer["customer_id"], bank_transfer)
        return {"message": transfer}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message("post_bank_transfer (depot_financial_apis.py)", str(e))
        raise HTTPException(status_code=422, detail=error_msg_no_service)
