from pydantic import BaseModel

class Pagination(BaseModel):
    page: int
    limit: int