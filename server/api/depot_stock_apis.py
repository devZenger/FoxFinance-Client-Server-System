from typing import Annotated

from fastapi import Depends,APIRouter
from pydantic import BaseModel


from service import User, get_current_active_user, search_stock

router = APIRouter()

class User(BaseModel):
    #username: str
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None

print("debug test")

@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term:str, current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    useremail = current_customer
    print(f"usermail: {useremail}")
    print ("/stocksearch")
    print(search_term)
    
    result = search_stock(search_term)
        
        
        
    return {"message":result}