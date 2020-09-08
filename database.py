import os
import databases
import sqlalchemy
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://")
# DATABASE_URL = "postgresql://user:password@postgresserver/db"


database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata = sqlalchemy.MetaData()
