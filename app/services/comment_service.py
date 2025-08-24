from sqlalchemy.orm import Session
from app.db.tables import Comment

def create_comment(db: Session, user_id: int, post_id: int, content: str):
    comment = Comment(user_id=user_id, post_id=post_id, content=content)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id.is_(comment_id)).first()

def delete_comment(db: Session, comment_id: int):
    comment = get_comment(db, comment_id)
    if comment:
        db.delete(comment)
        db.commit()
    return comment
