from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.comment import PagedComments
from app.models.post import PagedPosts
from app.models.user import UserInfo
from app.services.auth_service import get_user_by_id
from app.services.comment_service import get_comments, to_comment_list
from app.services.models_services import to_user_info
from app.services.post_service import get_posts, to_post_list

user_router = APIRouter(prefix="/users", tags=["user"])

@user_router.get("/{user_id}", response_model=UserInfo)
def get_user_account(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return to_user_info(db,get_user_by_id(db,user_id))

@user_router.get("/{user_id}/posts", response_model=PagedPosts)
def get_user_posts(
        user_id: int,
        page: int = 0,
        limit: int = 25,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user = get_user_by_id(db, user_id)
    posts = get_posts(db,user.id, page, limit)
    return PagedPosts(
        posts=to_post_list(db,posts),
        page= page,
        limit=limit
    )

@user_router.get("/{user_id}/comments", response_model=PagedComments)
def get_user_comments(
        user_id: int,
        page: int = 0,
        limit: int = 25,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user = get_user_by_id(db, user_id)
    comments = get_comments(db, user.id, page, limit)
    return PagedComments(
        comments=to_comment_list(db, comments),
        page=page,
        limit=limit
    )