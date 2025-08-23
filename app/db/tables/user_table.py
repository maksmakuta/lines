from sqlalchemy import Column, Integer, String
from .base_table import BaseTable

class UserTable(BaseTable):
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
