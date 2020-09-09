from pydantic import BaseModel


class Product(BaseModel):
    name: str
    author_id: int
    category_id: int
