import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASS")
database = os.getenv("DB_NAME")
encoded_passwd = quote_plus(passwd)

database_url = f"mysql+mysqlconnector://{user}:{encoded_passwd}@{host}/{database}"

engine = create_engine(database_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
