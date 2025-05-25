from fastapi import APIRouter, HTTPException

from utilitys import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import all_order_charges

router = APIRouter()


@router.get("/information/")
async def get_information():

    try:
        charges = all_order_charges()
        return {"message": charges}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
