from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AccountForm(BaseModel):
    last_name: str
    first_name: str
    street: str
    house_number: str
    zip_code: int
    city: str
    birthday: str
    email: str
    phone_number: str
    reference_account: str
    password: str
    

@router.post("create_account")
async def create_account(accountform: AccountForm):
    return {"message": "Accoount created"}