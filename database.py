import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_host = os.getenv("DATABASE_HOST")


# Create base for ORM
Base = declarative_base()

# Create engine using database url
DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(DATABASE_URL, echo=True)

# Create a session to interact with the database
db_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
