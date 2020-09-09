import sqlalchemy
from ..database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("disabled", sqlalchemy.Boolean, default=False),
)
