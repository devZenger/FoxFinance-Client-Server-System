import os
from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from repository import get_auth_datas, update_login_time
from schemas import User

_secret_key = None
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_token_key():
    global _secret_key
    if _secret_key is None:
        path = os.path.join("..", "server", "keys", "demo_token.key")
        try:
            with open(path, "rb") as key_file:
                secret_key_bytes = key_file.read()
                _secret_key = secret_key_bytes.decode("utf-8")
            return _secret_key
        except FileNotFoundError as e:
            error_msg = ("'demo_account.key' konnte nicht geöffnet werden.\n"
                         f"Pfad: {path}\n"
                         f"Error: {str(e)}\n")
            raise RuntimeError(error_msg) from e

    return _secret_key


def _verify_password(input_password: str, hashed_password: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(input_password, hashed_password)


def authenticate_customer(email: str, password: str, client_ip: str):

    db_query = get_auth_datas(email)

    if not db_query:
        return False, True
    if db_query["disabled"]:
        return False, True
    if db_query["email"] != email:
        return False, False
    if not _verify_password(password, db_query["password"]):
        return False, False
    db_query["client_ip"] = client_ip
    # login time to database
    update_login_time(db_query["customer_id"], db_query["client_ip"])

    return db_query, False


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    credtials_execption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Atuthenticate": "Bearer"},
    )
    try:
        token_key = get_token_key()
        payload = jwt.decode(token, token_key, algorithms=[ALGORITHM])

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
    token_key = get_token_key()
    return jwt.encode(to_encode, token_key, algorithm=ALGORITHM)
