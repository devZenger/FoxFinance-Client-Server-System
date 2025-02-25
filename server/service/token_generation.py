from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from pydantic import BaseModel

from repository import AuthData

SECRET_KEY = "fefbda68bb1af51ee7c4295f509b570a1aa96b01b754c4d50b52bdb3c17d7643"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
   username: str | None = None
   
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def get_user(email: str):
    db = AuthData()
    user_dict = db.get_data(email)
    return user_dict


#def get_user(db, username:str):
 #   if username in db:
  #      user_dict = db[username]
   #     return UserInDB(**user_dict)
    

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user





async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)], 
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user