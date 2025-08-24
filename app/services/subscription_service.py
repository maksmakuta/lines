from sqlalchemy.orm import Session
from app.db.tables import Subscription

def subscribe_user(db: Session, subscriber_id: int, target_id: int):
    sub = Subscription(subscriber_id=subscriber_id, target_id=target_id)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub

def unsubscribe_user(db: Session, subscriber_id: int, target_id: int):
    sub = (
        db.query(Subscription)
        .filter(Subscription.subscriber_id.is_(subscriber_id),
                Subscription.target_id.is_(target_id))
        .first()
    )
    if sub:
        db.delete(sub)
        db.commit()
    return sub

def get_subscriptions(db: Session, subscriber_id: int):
    return db.query(Subscription).filter(Subscription.subscriber_id.is_(subscriber_id)).all()
