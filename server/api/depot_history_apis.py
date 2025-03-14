from typing import Annotated

from fastapi import Depends,APIRouter, HTTPException
from pydantic import BaseModel


from service import User, get_current_active_user, depot_overview, past_transactions

router = APIRouter()

class User(BaseModel):
    #username: str
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None



@router.get("/depot/depotoverview/")
async def get_depot_overview(current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    try:     
        depot = depot_overview(current_customer["customer_id"])
        return {"message": depot}
    
    except Exception as e:
        
        raise HTTPException(status_code=422, detail=e)
    

@router.get("/depot/pasttransactions/{search_start}{search_end}")
async def get_past_transactions(search_start:str, search_end:str, current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    try:     
        transactions = past_transactions(current_customer["customer_id"], search_start, search_end)
        return {"message": transactions}
    
    except Exception as e:
        
        raise HTTPException(status_code=422, detail=e)   
