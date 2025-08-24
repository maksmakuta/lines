from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.post import NewPost, PostItem, PostDetailsItem
from app.models.response import DeleteResponse
from app.services.post_service import create_post, to_post_item, remove_post, get_detailed_post

post_router = APIRouter(prefix="/posts", tags=["posts"])

@post_router.put("/", response_model=PostItem)
def new_post(
        post_data: NewPost,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    post = create_post(db,current_user.id,post_data.body)
    return to_post_item(db,post)

@post_router.get("/{post_id}", response_model=PostDetailsItem)
def get_post(
        post_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    post = get_detailed_post(db, post_id)
    if post:
        return post
    raise HTTPException(
        status_code=404,
        detail="Post is not found"
    )

@post_router.delete("/{post_id}", response_model=DeleteResponse)
def delete_post(
        post_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    post = remove_post(db, post_id)
    return DeleteResponse(
        status = (post is not None),
        deleted_id = post_id
    )