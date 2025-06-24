from fastapi import APIRouter, HTTPException, status, Request

from utilities import exceptions_handler
from logger import error_login_message
from service import (authenticate_customer,
                     create_access_token,
                     create_validation,
                     activate_account,
                     make_registration)
from schemas import EmailOAuth2PasswordRequestForm, Token, Code, AccountForm

router = APIRouter()


def _request_ip(client_ip):

    if not client_ip:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Keine Ip-Adresse",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return client_ip


@router.post("/token")
async def customer_login_for_access_token(login_form: EmailOAuth2PasswordRequestForm, request: Request) -> Token:

    try:
        client_ip = _request_ip(request.client.host)
        customer, disabled = authenticate_customer(login_form.email, login_form.password, client_ip)

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

    except Exception as e:
        exceptions_handler(e, "customer_login_for_access_tokenä() (registration_and_auth_apis.py)")


@router.post("/create_customer_account/")
async def create_account(account_form: AccountForm, request: Request) -> None:

    try:
        client_ip = _request_ip(request.client.host)
        new_account = account_form.model_dump()
        make_registration(new_account, client_ip)

    except Exception as e:
        exceptions_handler(e, "create_account() (registration_and_auth_apis.py)")


@router.get("/startvalidation/{email}/")
async def get_validation(email: str):

    try:
        validation = create_validation(email)
        return {"message": validation}

    except Exception as e:
        exceptions_handler(e, "get_validation() (registration_and_auth_apis.py)")


@router.post("/activateaccount/")
async def post_activate_account(code: Code):

    code = code.model_dump()
    try:
        transmission = activate_account(code)
        return {"message": transmission}

    except Exception as e:
        exceptions_handler(e, "post_active_account() (registration_and_auth_apis.py)")
