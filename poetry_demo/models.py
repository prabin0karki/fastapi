import sqlalchemy
from .database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=1),
    sqlalchemy.Column("disabled", sqlalchemy.Boolean, default=0),
)

categories = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True, index=True),
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("author_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("category_id", sqlalchemy.ForeignKey("categories.id")),
    sqlalchemy.Column("is_available", sqlalchemy.Boolean, default=1),
)
