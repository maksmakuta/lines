from sqlalchemy.orm import Session

from app.db.tables import Like
from app.models.like import LikeItem


def like_post(db: Session, user_id: int, post_id: int):
    like = Like(user_id=user_id, post_id=post_id)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def like_comment(db: Session, user_id: int, comment_id: int):
    like = Like(user_id=user_id, comment_id=comment_id)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def unlike(db: Session, like_id: int):
    like = db.query(Like).filter(Like.id.is_(like_id)).first()
    if like:
        db.delete(like)
        db.commit()
    return like


def to_like(like: Like) -> LikeItem:
    return LikeItem(
        like_id=like.id,
        user_id=like.user_id,
        post_id=like.post_id,
        comment_id=like.comment_id,
    )
