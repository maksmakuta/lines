from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.tables import User, Post, Comment, Like
from app.models.user import UserInfo

def get_user_statistics(db: Session, user_id: int) -> dict:
    posts_count = db.query(func.count(Post.id)).filter(Post.user_id == user_id).scalar()
    comments_count = db.query(func.count(Comment.id)).filter(Comment.user_id == user_id).scalar()
    likes_count = db.query(func.count(Like.id)).filter(Like.user_id == user_id).scalar()

    return {
        "posts": posts_count or 0,
        "comments": comments_count or 0,
        "likes": likes_count or 0,
    }

def to_user_info(db: Session, user: User) -> UserInfo:
    stat = get_user_statistics(db,user.id)
    return UserInfo(
        user_id=user.id,
        name=user.username,
        mail=user.mail,
        created_at=user.registered_at,
        posts_count=stat.get("posts"),
        comments_count=stat.get("comments"),
        likes_count=stat.get("likes")
    )