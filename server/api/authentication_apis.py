from fastapi import APIRouter, HTTPException, status

from utilities import DBOperationError, SQlExecutionError, error_msg_no_service
from logger import error_message, error_login_message
from service import (Authentication,
                     create_access_token,
                     create_validation,
                     activate_account)
from schemas import EmailOAuth2PasswordRequestForm, Token, Code

router = APIRouter()


@router.post("/token")
async def customer_login_for_access_token(
        login_form: EmailOAuth2PasswordRequestForm) -> Token:

    authentication = Authentication()

    customer, disabled = authentication.authenticate_customer(login_form.email, login_form.password)

    if disabled:
        error_login_message("<Fehlerhafter Login-Versuch mit nicht existierenden oder gesperrten Account")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account existiert nicht oder ist gesperrt",
            headers={"WWW-Authenticate": "Bearer"},
            )

    if not customer:
        error_login_message("Fehlerhafter Login-Versuch mit falschen Passwort oder Email Adresse")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falsches Passwort oder Email Adresse",
            headers={"WWW-Authenticate": "Bearer"},
            )

    return Token(access_token=await create_access_token(customer), token_type="bearer")


@router.get("/startvalidation/{email}/")
async def get_validation(email: str):

    try:
        validation = create_validation(email)
        return {"message": validation}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message("get_validation (authentication_apis.py)", str(e))
        raise HTTPException(status_code=422, detail=error_msg_no_service)


@router.post("/activateaccount/")
async def post_activate_account(code: Code):

    try:
        transmission = activate_account(code)
        return {"message": transmission}

    except DBOperationError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except SQlExecutionError as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
    except Exception as e:
        error_message(e)
        raise HTTPException(status_code=422, detail=error_msg_no_service)
