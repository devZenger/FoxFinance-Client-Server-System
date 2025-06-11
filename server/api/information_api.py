from fastapi import APIRouter

from utilities import excptions_handler
from service import all_order_charges

router = APIRouter()


@router.get("/information/")
async def get_information():

    try:
        charges = all_order_charges()
        return {"message": charges}

    except Exception as e:
        excptions_handler(e, "get_information() (information_api.py)")
