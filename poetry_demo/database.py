import os
import sys
import databases
import sqlalchemy
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)
# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = os.environ["DATABASE_URL"]


database = databases.Database(DATABASE_URL)

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = sqlalchemy.create_engine(DATABASE_URL)


metadata = sqlalchemy.MetaData()
