from sqlalchemy.orm import Session
from app.db.tables import Post

def create_post(db: Session, user_id: int, content: str):
    post = Post(user_id=user_id, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, user_id: int, page: int = 0, limit: int = 25):
    return (db
            .query(Post)
            .filter(Post.author == user_id)
            .offset(page * limit)
            .limit(limit)
            .all())

def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if post:
        db.delete(post)
        db.commit()
    return post

def get_feed_posts(db: Session, user_ids: list[int]):
    return (
        db.query(Post)
        .filter(Post.user_id.in_(user_ids))
        .order_by(Post.created_at.desc())
        .all()
    )
