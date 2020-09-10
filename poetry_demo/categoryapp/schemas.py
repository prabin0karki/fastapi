from pydantic import BaseModel


class Category(BaseModel):
    name: str


class CategoryIn(Category):
    id: int
