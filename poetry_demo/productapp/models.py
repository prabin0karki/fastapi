import sqlalchemy
from ..database import metadata

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column(
        "author_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
        nullable=False,
    ),
    sqlalchemy.Column(
        "category_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("categories.id"),
        nullable=False,
    ),
    sqlalchemy.Column("is_available", sqlalchemy.Boolean, default=1),
)
