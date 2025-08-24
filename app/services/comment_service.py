from sqlalchemy.orm import Session

from app.db.tables import Comment
from app.models.comment import CommentItem
from app.services.auth_service import get_user_by_id


def create_comment(db: Session, user_id: int, post_id: int, content: str):
    comment = Comment(user_id=user_id, post_id=post_id, content=content)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comments(db: Session, user_id: int, page: int = 0, limit: int = 25):
    return (db
            .query(Comment)
            .filter(Comment.user_id == user_id)
            .offset(page * limit)
            .limit(limit)
            .all())


def get_comment_by_id(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id.is_(comment_id)).first()


def remove_comment(db: Session, comment_id: int):
    comment = get_comment_by_id(db, comment_id)
    if comment:
        db.delete(comment)
        db.commit()
    return comment

def to_comment_item(db: Session,p: Comment):
    return CommentItem(
        id = p.id,
        author = get_user_by_id(db,p.user_id).username,
        body = p.content,
        likes = len(p.likes),
        created_at = p.created_at
    )

def to_comment_list(db: Session,comments : list[Comment]) -> list[CommentItem]:
    res = []
    for p in comments:
        res.append(to_comment_item(db,p))
    return res