from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_ative: Optional[bool] = None
    disabled: Optional[bool] = None


class UserCreate(User):
    password: str
