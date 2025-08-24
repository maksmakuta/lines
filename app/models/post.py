from datetime import datetime
from pydantic import BaseModel

from app.models.pagination import Pagination


class PostItem(BaseModel):
    id: int
    author: str
    body: str
    likes: int
    comments: int
    created_at: datetime

class PostDetailsItem(BaseModel):
    id: int
    author: str
    body: str
    likes_ids: list[int]
    comments_ids: list[int]
    created_at: datetime

class NewPost(BaseModel):
    body: str

class PagedPosts(Pagination):
    posts: list[PostItem]