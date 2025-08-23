from datetime import datetime
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    post: int
    author: int
    text: str
    created_at: datetime

class NewComment(BaseModel):
    post: int
    author: int
    text: str
