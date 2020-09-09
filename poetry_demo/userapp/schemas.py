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


class UserCreate(User):
    password: str


class UserIn(User):
    id: int
    is_active: bool
    disabled: bool
