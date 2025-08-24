from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables import User
from app.deps import get_current_user
from app.models.response import DeleteResponse
from app.models.subscription import SubscriptionItem
from app.services.subscription_service import subscribe_user, to_sub_item, unsubscribe_user

sub_router = APIRouter(prefix="/sub", tags=["subscriptions"])


@sub_router.put("/", response_model=SubscriptionItem)
def subscribe(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    sub = subscribe_user(db, current_user.id, user_id)
    return to_sub_item(db, sub)


@sub_router.delete("/{subscription_id}", response_model=DeleteResponse)
def unsubscribe(
        subscription_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    sub = unsubscribe_user(db, subscription_id)
    return DeleteResponse(
        status=(sub is not None),
        deleted_id=subscription_id
    )
