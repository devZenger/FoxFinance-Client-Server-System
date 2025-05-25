from pydantic import BaseModel


class EmailOAuth2PasswordRequestForm(BaseModel):
    email: str
    password: str


class LoginForm(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Code(BaseModel):
    validation_number: int


class User(BaseModel):
    email: str
    customer_id: int | None = None
    disabled: bool | None = None
