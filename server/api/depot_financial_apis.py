from typing import Annotated

from fastapi import Depends,APIRouter, HTTPException
from pydantic import BaseModel

from service import User, get_current_active_user, get_customer_balance, do_past_fin_transactions, make_bank_transfer

router = APIRouter()


class User(BaseModel):
    email: str
    customer_id: int | None = None
    disabled: bool | None = None


class BankTransfer(BaseModel):
    fin_amount: float
    transfer_type: str
    usage: str | None = None


@router.get("/depot/current_balance/")
async def get_current_balance(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        current_balance = get_customer_balance(current_customer["customer_id"])
        return {"message": current_balance}

    except Exception as e:

        raise HTTPException(status_code=422, detail=str(e))


@router.get("/depot/pastfinancialtransactions/{search_start}/{search_end}")
async def get_past_financial_transactions(search_start:str, search_end:str, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        transactions = do_past_fin_transactions(current_customer["customer_id"], search_start, search_end)
        return {"message": transactions}

    except Exception as e:

        raise HTTPException(status_code=422, detail=str(e))


@router.post("/depot/banktransfer/")
async def post_bank_transfer(bank_transfer:BankTransfer, current_customer: Annotated[User, Depends(get_current_active_user)]):

    print(f"bank transfer: {bank_transfer}")

    try:
        transfer = make_bank_transfer(current_customer["customer_id"], bank_transfer)
        return {"message": transfer}

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
