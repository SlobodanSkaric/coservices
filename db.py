import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALYHEMY_DATABASE_URL = "postgresql://postgres:admin81@localhost/coservices"

engine = create_engine(SQLALYHEMY_DATABASE_URL)
sessions_local = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessions_local()
    try:
        yield db
    finally:
        db.close()