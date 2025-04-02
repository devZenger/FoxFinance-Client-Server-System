import jwt
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

from service import Authentication, create_access_token, create_validation, activate_account


class EmailOAuth2PasswordRequestForm(BaseModel):
    email: str
    password: str


router = APIRouter()


class LoginForm(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Code(BaseModel):
    validation_number: int




@router.post("/token")
async def customer_login_for_access_token(
    login_form: EmailOAuth2PasswordRequestForm) -> Token:

    authentication = Authentication()

    customer = authentication.authenticate_customer(login_form.email, login_form.password)

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falsches Passwort oder Email Adresse",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return Token(access_token = await create_access_token(customer), token_type="bearer")


@router.get("/startvalidation/{email}/")
async def get_validation(email:str):

    print("email", email)

    try:
        validation = create_validation(email)
        return {"message":validation}

    except Exception as e:
        print(f"HTTPException detail: {e}")
        raise HTTPException(status_code=422, detail=str(e))

@router.post("/activateaccount/")
async def post_activate_account(code:Code):

    try:
        transmission = activate_account(code)
        return {"message":transmission}

    except Exception as e:    
        print(f"HTTPException detail: {e}")
        raise HTTPException(status_code=422, detail=str(e))
