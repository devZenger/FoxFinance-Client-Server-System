from pydantic import BaseModel


class AccountForm(BaseModel):
    last_name: str
    first_name: str
    street: str
    house_number: str
    zip_code: int
    city: str
    birthday: str
    email: str
    phone_number: str
    reference_account: str
    fin_amount: float
    password: str


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
