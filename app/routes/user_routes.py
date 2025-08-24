from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.user import UserInfo
from app.services.auth_service import get_user_by_id
from app.services.models_services import to_user_info

user_router = APIRouter(prefix="/users", tags=["user"])

@user_router.get("/{user_id}", response_model=UserInfo)
def get_user_account(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return to_user_info(db,get_user_by_id(db,user_id))

@user_router.get("/{user_id}/posts")
def get_user_posts(
        user_id: int,
        page: int,
        limit: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user = get_user_by_id(db, user_id)
    get_user_posts(db,)

@user_router.get("/user_id}/comments")
def get_user_comments(user_id: int):
    pass

@user_router.get("/user_id}/likes")
def get_user_likes(user_id: int):
    pass
