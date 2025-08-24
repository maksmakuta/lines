from datetime import datetime
from pydantic import BaseModel

from app.models.pagination import Pagination


class CommentItem(BaseModel):
    id: int
    author: str
    body: str
    likes: int
    created_at: datetime

class NewComment(BaseModel):
    post_id: int
    body: str

class PagedComments(Pagination):
    comments: list[CommentItem]