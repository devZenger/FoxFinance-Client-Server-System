from typing import Annotated

from fastapi import Depends,APIRouter, HTTPException
from pydantic import BaseModel


from service import User, Settings, get_current_active_user

router = APIRouter()

class User(BaseModel):
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None


class Settings(BaseModel):
    transmission_type: str
    street: str | None = None
    house_number: str | None = None
    city: str | None = None
    zip_code: str | None = None
    phone_number: str | None = None
    email: str | None = None
    reference_account: str | None = None
    password: str | None = None


@router.get("/depot/settings/")
async def get_settings(search_term:str, current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    pass
     
    

@router.post("/depot/changesettings/")
async def trade_stocks(settings: Settings, current_customer: Annotated[User, Depends(get_current_active_user)]):
 
    pass