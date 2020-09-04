from sqlalchemy.orm import Session

import models, schemas
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from database import SessionLocal

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
from models import User

#verify if password match with hashed_password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#generate a hash password
def get_password_hash(password):
    return pwd_context.hash(password)


#access a user ingo by a email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()



#create a user or register a user
def create_user(db: Session, user: schemas.UserCreate):
    password = get_password_hash(user.password)
    db_user = models.User(email=user.email, password=password,\
        first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



#authenticate_user before create a token
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
