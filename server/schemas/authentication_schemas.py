from pydantic import BaseModel, field_validator


class EmailOAuth2PasswordRequestForm(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Code(BaseModel):
    validation_number: int

    @field_validator("validation_number")
    @classmethod
    def validate_number(cls, v):
        if v > 99_999 and v < 1_000_000:
            return v
        else:
            raise ValueError("Falsche Validationsnummer.")


class User(BaseModel):
    email: str
    customer_id: int | None = None
    disabled: bool | None = None
