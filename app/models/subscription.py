from pydantic import BaseModel

from app.models.pagination import Pagination
from app.models.user import UserInfo


class SubscriptionItem(BaseModel):
    id: int
    target: UserInfo


class PagedSubscriptions(Pagination):
    subs: list[SubscriptionItem]
