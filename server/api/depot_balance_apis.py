from typing import Annotated

from fastapi import Depends,APIRouter, HTTPException
from pydantic import BaseModel


from service import User, get_current_active_user, get_customer_balance, get_past_balance_transactions

router = APIRouter()

class User(BaseModel):
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None

class CashTransfer(BaseModel):
    sum: int
    transaction_type: str
    

@router.get("/depot/current_balance/")
async def get_current_balance(current_customer: Annotated[User, Depends(get_current_active_user)]):
     
    try:     
        current_balance = get_customer_balance(current_customer.customer_id) 
        return {"message": current_balance}
    
    except Exception as e:
        
        raise HTTPException(status_code=422, detail=e)
    

@router.get("/depot/pastbalancetransactions/{search_start}{search_end}")
async def get_past_balance_transactions(search_start:str, search_end:str, current_customer: Annotated[User, Depends(get_current_active_user)]):
     
    try:     
        transactions = get_past_balance_transactions(current_customer.customer_id, search_start, search_end)
        return {"message": transactions}
    
    except Exception as e:
        
        raise HTTPException(status_code=422, detail=e)
    
#@router.post("/depot/cashtransfer")
#async def post_cash_transfer(cash_transfer:CashTransfer, current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    


