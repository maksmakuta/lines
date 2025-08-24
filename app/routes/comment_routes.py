from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.comment import NewComment, CommentItem
from app.models.response import DeleteResponse
from app.services.comment_service import create_comment, to_comment_item, get_comment_by_id, remove_comment

comment_router = APIRouter(prefix="/comment", tags=["comments"])


@comment_router.put("/", response_model=CommentItem)
def new_comment(
        comment_data: NewComment,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    comment = create_comment(db, current_user.id, comment_data.post_id, comment_data.body)
    return to_comment_item(db, comment)


@comment_router.get("/{comment_id}", response_model=CommentItem)
def get_comment(
        comment_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    comment = get_comment_by_id(db, comment_id)
    if comment:
        return to_comment_item(db, comment)
    raise HTTPException(
        status_code=404,
        detail="Comment is not found"
    )


@comment_router.delete("/{comment_id}", response_model=DeleteResponse)
def delete_comment(
        comment_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    comment = remove_comment(db, comment_id)
    return DeleteResponse(
        status=(comment is not None),
        deleted_id=comment_id
    )
