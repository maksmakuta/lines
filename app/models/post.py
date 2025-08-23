from pydantic import BaseModel

class Post(BaseModel):
    id: int
    title: str
    body: str

class NewPost(BaseModel):
    title: str
    body: str
