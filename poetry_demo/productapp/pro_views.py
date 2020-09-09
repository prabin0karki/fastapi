from typing import List
from fastapi import APIRouter, HTTPException
from ..database import database
from .models import products
from .schemas import Product
from fastapi import Depends
from ..userapp.crud import get_current_active_user
from ..userapp.schemas import User

router = APIRouter()


@router.post("/product/", response_model=Product)
async def create_user(
    product: Product, current_user: User = Depends(get_current_active_user)
):
    query = products.select().where(products.c.name == product.name)
    product_obj = await database.fetch_one(query=query)
    if not product_obj:
        query = products.insert().values(
            name=product.name,
            author_id=product.author_id,
            category_id=product.category_id,
        )
        last_record_id = await database.execute(query)
        return {**product.dict(), "id": last_record_id}
    raise HTTPException(
        status_code=400, detail="Category with that name already registered"
    )


@router.get("/products/", response_model=List[Product])
async def read_users(current_user: User = Depends(get_current_active_user)):
    query = products.select()
    return await database.fetch_all(query=query)
