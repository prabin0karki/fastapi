import databases
import sqlalchemy
# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql://prabin:prabin@localhost/project_db"


database = databases.Database(DATABASE_URL)

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = sqlalchemy.create_engine(
    DATABASE_URL
)


metadata = sqlalchemy.MetaData()
