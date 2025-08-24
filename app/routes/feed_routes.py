from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.services.post_service import get_feed_posts
from app.services.subscription_service import get_subscriptions

feed_router = APIRouter(tags=["feed"])

@feed_router.get("/feed")
def get_feed(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    subscriptions = get_subscriptions(db, current_user.id)
    subscribed_ids = [sub.target_id for sub in subscriptions]
    posts = get_feed_posts(db, subscribed_ids)
    return posts