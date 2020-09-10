from typing import List
from fastapi import APIRouter, HTTPException
from ..database import database
from .models import products
from .schemas import Product, ProductIn
from fastapi import Depends
from ..userapp.crud import get_current_active_user
from ..userapp.schemas import User
from loguru import logger

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
            price=product.price,
        )
        last_record_id = await database.execute(query)
        return {**product.dict(), "id": last_record_id}
    raise HTTPException(
        status_code=400, detail="Product with that name already registered"
    )


@router.get("/products/", response_model=List[ProductIn])
async def read_users(current_user: User = Depends(get_current_active_user)):
    query = products.select()
    return await database.fetch_all(query=query)


@router.delete("/products/{product_id}")
async def delete_product(
    product_id: int, current_user: User = Depends(get_current_active_user)
):
    query = products.select().where(products.c.id == product_id)
    product_obj = await database.fetch_one(query=query)
    if product_obj:
        query = products.delete().where(products.c.id == product_id)
        response = await database.execute(query)
        logger.info("Response from the server {}".format(response))
        return {"msg": "Product deleted successfully"}
    raise HTTPException(status_code=400, detail="Product id do not match.")


@router.put("/products/{product_id}", response_model=Product)
async def edit_product(
    product_id: int,
    product: Product,
    current_user: User = Depends(get_current_active_user),
):
    query = products.select().where(products.c.id == product_id)
    product_obj = await database.fetch_one(query=query)
    if product_obj:
        query = (
            products.update()
            .where(products.c.id == product_id)
            .values(
                name=product.name,
                author_id=product.author_id,
                category_id=product.category_id,
                price=product.price,
            )
        )
        last_record_id = await database.execute(query)
        return {**product.dict(), "id": last_record_id}
    raise HTTPException(status_code=400, detail="Product id do not match.")
