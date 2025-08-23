from datetime import datetime
from pydantic import BaseModel

class Like(BaseModel):
    id: int
    author: int
    post: int
    created_at: datetime

class NewLike(BaseModel):
    author: int
    post: int
