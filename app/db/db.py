from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables.base_table import BaseTable
from .tables.user_table import UserTable
from .tables.secret_table import SecretTable
from ..config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
BaseTable.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()