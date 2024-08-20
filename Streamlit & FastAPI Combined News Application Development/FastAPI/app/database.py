import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{passwd}@{host}/{db}".format(
    user=os.getenv("DB_USER"),
    passwd=quote_plus(os.getenv("DB_PASS")),
    host=os.getenv("DB_HOST"),
    db=os.getenv("DB_NAME")
)

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
