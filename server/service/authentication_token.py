from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel


from repository import get_auth_datas, insert_login_time

SECRET_KEY = "fefbda68bb1af51ee7c4295f509b570a1aa96b01b754c4d50b52bdb3c17d7643"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
   email: str | None = None
    

class User(BaseModel):
    #username: str
    email: str
    #full_name: str | None = None
    disabled: bool | None = None  

  
#def get_costumer_data(email: str):
 #       search = AuthData()
  #      user_dict = search.get_data(email)
   #     return user_dict


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



class Authentication: 
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def verify_password(self, input_password, hashed_password):
        return self.pwd_context.verify(input_password, hashed_password)
    
    def authenticate_customer(self, email:str, password:str):
        
        print(f"ausgabe email in line 58 {email}")
        db_query = get_auth_datas(email)
        print(f"ausgage von db_query: {db_query}")
        print(db_query)
        
        if not db_query:
            return False
        if db_query["email"] != email:
            return False
        if not self.verify_password(password, db_query["password"]):
            return False
        
        #login time to database
        insert_login_time(db_query["customer_id"])
        
        
        return db_query



    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credtials_execption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Atuthenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"payload {payload}")
        email = payload.get("sub")
        print(f"username: {email}")
        if email is None:
            raise credtials_execption
        token_data = TokenData(email = email)
    except InvalidTokenError:
        raise credtials_execption
    print(f"token data {token_data}")
    print(f"token data.email {token_data.email}")
    email = get_auth_datas(email=token_data.email)
    if email is None:
        raise credtials_execption
    return email

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):  
    print(type(current_user))
    print(f"currend_user {current_user}")
    print(type(current_user))
    current_user["disabled"] = False
    print(f"currend_user2 {current_user}")
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def create_access_token(user):
    expires_delta = timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user}
    
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
  
        
        
        