from typing import Optional
from pydantic import BaseModel, field_validator
from utilities import (check_len_bg2,
                       check_house_number,
                       check_zip_code,
                       check_birthday,
                       check_email,
                       check_phone_number,
                       check_fin_amount,
                       check_password,
                       bank_account_encode)


class AccountForm(BaseModel):
    last_name: str
    first_name: str
    birthday: str

    street: str
    house_number: str
    city: str
    zip_code: int

    email: str
    phone_number: str

    fin_amount: float
    reference_account: str

    password: str

    # Validation

    @field_validator("last_name", "first_name", "street", "city")
    @classmethod
    def validate_names(cls, v, info):
        return check_len_bg2(v)

    @field_validator("birthday")
    @classmethod
    def validate_birthday(cls, v):
        return check_birthday(v)

    @field_validator("house_number")
    @classmethod
    def validate_house_number(cls, v):
        return check_house_number(v)

    @field_validator("zip_code")
    @classmethod
    def validate_zip_code(cls, v):
        return check_zip_code(v)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        return check_email(v)

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v):
        return check_phone_number(v)

    @field_validator("fin_amount")
    @classmethod
    def validate_fin_amount(cls, v):
        return check_fin_amount(v)

    @field_validator("reference_account")
    @classmethod
    def validate_bank_account(cls, v):
        value = check_len_bg2(v)
        return bank_account_encode(value)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        return check_password(v)


class Settings(BaseModel):
    street: Optional[str] = None
    house_number: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[int] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    reference_account: Optional[str] = None
    password: Optional[str] = None

    # Validation

    @field_validator("street", "city")
    @classmethod
    def validate_names(cls, v, info):
        return check_len_bg2(v)

    @field_validator("house_number")
    @classmethod
    def validate_house_number(cls, v):
        return check_house_number(v)

    @field_validator("zip_code")
    @classmethod
    def validate_zip_code(cls, v):
        return check_zip_code(v)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        return check_email(v)

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v):
        return check_phone_number(v)

    @field_validator("reference_account")
    @classmethod
    def validate_bank_account(cls, v):
        value = check_len_bg2(v)
        return bank_account_encode(value)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        return check_password(v)