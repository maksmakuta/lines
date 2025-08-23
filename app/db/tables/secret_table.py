from sqlalchemy import Column, Integer, String
from .base_table import BaseTable

class SecretTable(BaseTable):
    __tablename__ = "secrets"
    user_id = Column(Integer, unique=True, primary_key=True, index=True)
    token = Column(String, unique=True, nullable=False, index=True)
