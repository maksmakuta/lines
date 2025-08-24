from pygments.styles.dracula import comment
from sqlalchemy.orm import Session
from app.db.tables import Post
from app.models.post import PostItem, PostDetailsItem
from app.services.auth_service import get_user_by_id


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
            .filter(Post.user_id == user_id)
            .offset(page * limit)
            .limit(limit)
            .all())

def remove_post(db: Session, post_id: int):
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

def to_post_item(db: Session,p: Post):
    return PostItem(
        id= p.id,
        author= get_user_by_id(db,p.user_id).username,
        body= p.content,
        likes= len(p.likes),
        comments=len(p.comments),
        created_at=p.created_at
    )

def to_post_list(db: Session,posts : list[Post]) -> list[PostItem]:
    res = []
    for p in posts:
        res.append(to_post_item(db,p))
    return res

def get_detailed_post(db: Session, post_id: int) -> PostDetailsItem | None:
    post = get_post(db, post_id)
    if post:
        return PostDetailsItem(
            id = post.id,
            author = get_user_by_id(db, post.user_id).username,
            body = post.content,
            likes_ids =  [like.id for like in post.likes],
            comments_ids =  [comment.id for comment in post.comments],
            created_at = post.created_at
        )
    else:
        return None
