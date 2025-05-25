from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from utilitys import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import (customer_name,
                     depot_overview,
                     past_transactions,
                     get_current_active_user)
from schemas import User

router = APIRouter()


@router.get("/depot/")
async def get_depot(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        name = customer_name(current_customer["customer_id"])
        return {"message": name}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.get("/depot/depotoverview/")
async def get_depot_overview(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        depot = depot_overview(current_customer["customer_id"])
        return {"message": depot}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.get("/depot/pasttransactions/{search_start}/{search_end}")
async def get_past_transactions(search_start: str,
                                search_end: str,
                                current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        transactions = past_transactions(current_customer["customer_id"], search_start, search_end)
        return {"message": transactions}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
