from fastapi import APIRouter, HTTPException

from utilities import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import CustomerRegistration
from schemas import AccountForm

router = APIRouter()


@router.post("/create_customer_account/")
async def create_account(account_form: AccountForm):

    try:
        customer_datas = CustomerRegistration()
        customer_datas.fill_in(account_form)
        customer_datas.insert_db()

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message("create_customer_account (create_customer_account_api.py)", (e))
        raise HTTPException(status_code=422, detail=str(e))
