from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from service import customer_name, get_current_active_user
from schemas import User

router = APIRouter()



@router.get("/depot/")
async def get_depot(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        name = customer_name(current_customer["customer_id"])
        return {"message": name}

    except Exception as e:

        raise HTTPException(status_code=422, detail=str(e))