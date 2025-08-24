from pydantic import BaseModel


class LikeItem(BaseModel):
    like_id: int
    post_id: int
    comment_id: int
    user_id: int

class NewLike(BaseModel):
    post_id: int
    comment_id: int