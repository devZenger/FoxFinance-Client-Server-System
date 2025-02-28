from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel

from service import Authentication, create_access_token


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
    

@router.post("/token")
async def customer_login_for_access_token(
    login_form: Annotated[EmailOAuth2PasswordRequestForm, Depends()],) -> Token:
    
    authentication = Authentication()
    customer = authentication.autheticate_customer(login_form.email, login_form.password)
    
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username oder password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    
    return Token(create_access_token(customer["email"]), token_type="bearer")
