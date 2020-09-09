import sqlalchemy
from ..database import metadata


categories = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True, index=True),
)
