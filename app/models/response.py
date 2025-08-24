from pydantic import BaseModel


class DeleteResponse(BaseModel):
    status: bool
    deleted_id: int