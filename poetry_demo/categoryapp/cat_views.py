from typing import List
from fastapi import APIRouter, HTTPException
from ..database import database
from .models import categories
from .schemas import Category
from fastapi import Depends
from ..userapp.crud import get_current_active_user
from ..userapp.schemas import User

router = APIRouter()


@router.post("/category/", response_model=Category)
async def create_user(
    category: Category, current_user: User = Depends(get_current_active_user)
):
    query = categories.select().where(categories.c.name == category.name)
    category_obj = await database.fetch_one(query=query)
    if not category_obj:
        query = categories.insert().values(name=category.name)
        last_record_id = await database.execute(query)
        return {**category.dict(), "id": last_record_id}
    raise HTTPException(
        status_code=400, detail="Category with that name already registered"
    )


@router.get("/categories/", response_model=List[Category])
async def read_users(current_user: User = Depends(get_current_active_user)):
    query = categories.select()
    return await database.fetch_all(query=query)
