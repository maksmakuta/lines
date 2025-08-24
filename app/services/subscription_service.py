from sqlalchemy.orm import Session

from app.db.tables import Subscription
from app.models.subscription import SubscriptionItem
from app.services.auth_service import get_user_by_id
from app.services.models_services import to_user_info


def subscribe_user(db: Session, subscriber_id: int, target_id: int):
    sub = Subscription(subscriber_id=subscriber_id, target_id=target_id)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub


def unsubscribe_user(db: Session, sub_id: int):
    sub = (
        db.query(Subscription)
        .filter(Subscription.id == sub_id)
        .first()
    )
    if sub:
        db.delete(sub)
        db.commit()
    return sub

def get_subscriptions(db: Session, subscriber_id: int):
    return db.query(Subscription).filter(Subscription.subscriber_id.is_(subscriber_id)).all()


def to_sub_item(db: Session, s: Subscription) -> SubscriptionItem:
    return SubscriptionItem(
        id=s.id,
        target=to_user_info(db, get_user_by_id(db, s.target_id))
    )
