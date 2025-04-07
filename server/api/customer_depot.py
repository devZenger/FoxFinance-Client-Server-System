from typing import Annotated

from fastapi import Depends, APIRouter
from pydantic import BaseModel

from service import get_current_active_user

router = APIRouter()


class User(BaseModel):
    email: str
    customer_id: int | None = None
    disabled: bool | None = None

@router.get("/depot/")
async def get_depot(current_customer: Annotated[User, Depends(get_current_active_user)]):

    useremail = current_customer
    print(f"usermail: {useremail}")

    return {"message": "Fox Finance offers great service from /depot/"}
