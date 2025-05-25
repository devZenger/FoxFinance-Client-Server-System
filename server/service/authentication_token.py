import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from repository import get_auth_datas, insert_login_time
from schemas import User

# SECRET_KEY = "fefbda68bb1af51ee7c4295f509b570a1aa96b01b754c4d50b52bdb3c17d7643"
secret_key = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def load_token_key():

    global secret_key
    path = os.path.join("..", "server", "keys", "demo_token.key")
    try:
        with open(path, "rb") as key_file:
            secret_key_bytes = key_file.read()
        secret_key = secret_key_bytes.decode("utf-8")

    except FileNotFoundError as e:
        error_msg = ("'demo_account.key' konnte nicht geöffnet werden.\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e


class Authentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _verify_password(self, input_password: str, hashed_password: str):
        return self.pwd_context.verify(input_password, hashed_password)

    def authenticate_customer(self, email: str, password: str):

        db_query = get_auth_datas(email)

        if not db_query:
            return False, True
        if db_query["disabled"]:
            return False, True
        if db_query["email"] != email:
            return False, False
        if not self._verify_password(password, db_query["password"]):
            return False, False

        # login time to database
        insert_login_time(db_query["customer_id"])

        return db_query, False


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    credtials_execption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Atuthenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])

        email = payload.get("email")

        if email is None:
            raise credtials_execption

    except InvalidTokenError:
        print("raise credtials")
        raise credtials_execption

    user_dic = get_auth_datas(email=email)
    if user_dic.get("customer_id") is None:
        raise credtials_execption

    return user_dic


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):

    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def create_access_token(user: dict):
    expires_delta = timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = user.copy()

    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
