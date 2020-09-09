from typing import List
from fastapi import APIRouter, HTTPException
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from ..database import database
from .models import users
from .schemas import Token, User, UserCreate
from fastapi import Depends, status
from .crud import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_active_user,
    get_password_hash,
    authenticate_user,
)

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    query = users.select().where(users.c.email == user.email)
    user_obj = await database.fetch_one(query=query)
    if not user_obj:
        password = get_password_hash(user.password)
        query = users.insert().values(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=password,
            is_active=True,
            disabled=False,
        )
        last_record_id = await database.execute(query)
        return {**user.dict(), "id": last_record_id}
    raise HTTPException(status_code=400, detail="Email already registered")


@router.get("/users/", response_model=List[User])
async def read_users(current_user: User = Depends(get_current_active_user)):
    query = users.select()
    return await database.fetch_all(query)
    # return await database.fetch_one(query=query)
