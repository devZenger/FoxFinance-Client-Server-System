from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel
from service import User, SettingsService, get_current_active_user

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
async def get_settings(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        settings_service = SettingsService()
        current_settings = settings_service.search_current_settings(
            current_customer["customer_id"])

        return {"message": current_settings}

    except Exception as e:
        error = f"Fehler bei get_settings. Error: {e}"
        print(error)
        raise HTTPException(status_code=422, detail=str(error))


@router.post("/depot/changesettings/")
async def change_settings(settings: Settings, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        settings_service = SettingsService()
        settings_service.update_service(current_customer["customer_id"],
                                        settings)
        return {"message": "Updated"}

    except Exception as e:
        error = f"Fehler bei change_settings. Error: {e}"
        print(error)
        raise HTTPException(status_code=422, detail=(error))
