from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException

from utilitys import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message
from service import SettingsService, get_current_active_user
from schemas import User, Settings

router = APIRouter()


@router.get("/depot/settings/")
async def get_settings(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        settings_service = SettingsService()
        current_settings = settings_service.search_current_settings(current_customer["customer_id"])

        return {"message": current_settings}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.post("/depot/changesettings/")
async def change_settings(settings: Settings, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        settings_service = SettingsService()
        settings_service.update_service(current_customer["customer_id"], settings)
        return {"message": "Updated"}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
