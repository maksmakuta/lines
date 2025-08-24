from datetime import datetime

from pydantic import BaseModel

class UserInfo(BaseModel):
    user_id: int
    name: str
    mail: str
    posts_count: int
    comments_count: int
    likes_count: int
    created_at: datetime