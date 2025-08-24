from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.like import NewLike, LikeItem
from app.models.response import DeleteResponse
from app.services.like_service import like_post, to_like, like_comment, unlike

like_router = APIRouter(prefix="/like", tags=["likes"])


@like_router.put("/", response_model=LikeItem)
def new_like(
        like_data: NewLike,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if like_data.post_id > 0:
        like = like_post(db, current_user.id, like_data.post_id)
        return to_like(like)
    if like_data.comment_id > 0:
        like = like_comment(db, current_user.id, like_data.comment_id)
        return to_like(like)
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Like should have post_id or comment_id"
    )


@like_router.delete("/{like_id}")
def delete_like(
        like_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    like = unlike(db, like_id)
    return DeleteResponse(
        status=(like is not None),
        deleted_id=like_id
    )
