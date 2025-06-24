from fastapi import APIRouter

from utilities import exceptions_handler
from service import all_order_charges

router = APIRouter()


@router.get("/information/")
async def get_information():

    try:
        charges = all_order_charges()
        return {"message": charges}

    except Exception as e:
        exceptions_handler(e, "get_information() (information_api.py)")
