from schemas import User, UserCreate, Token
from crud import get_password_hash, get_current_active_user,\
    create_access_token, pwd_context, ACCESS_TOKEN_EXPIRE_MINUTES
from models import users
from database import database, engine, metadata
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    query = users.select().where(users.c.email == email)
    user = await database.fetch_one(query=query)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    if not pwd_context.verify(password, user.password):
        return False
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    query = users.select().where(users.c.email == user.email)
    user_obj = await database.fetch_one(query=query)
    if not user_obj:
        password = get_password_hash(user.password)
        query = users.insert().values(
            first_name=user.first_name,
            last_name=user.last_name, email=user.email,
            password=password)
        last_record_id = await database.execute(query)
        return {**user.dict(), "id": last_record_id}
    raise HTTPException(status_code=400, detail="Email already registered")


@app.get("/users/", response_model=User)
async def read_users(
        current_user: User = Depends(get_current_active_user)):
    query = users.select().where(users.c.email == current_user.email)
    return await database.fetch_one(query=query)
    # print("==============")
    # print(current_user)
    # query = users.select()
    # return await database.fetch_all(query)
    # return users
