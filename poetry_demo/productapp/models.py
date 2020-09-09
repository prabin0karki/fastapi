import sqlalchemy
from ..database import metadata

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("author_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("category_id", sqlalchemy.ForeignKey("categories.id")),
    sqlalchemy.Column("is_available", sqlalchemy.Boolean, default=1),
)
