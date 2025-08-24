from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    mail = Column(String,unique=True, nullable=False)
    password = Column(String, nullable=False)  # hash!
    token = Column(String, unique=True, nullable=True)
    registered_at = Column(DateTime, default=func.now(),nullable=False)

    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

    subscriptions = relationship("Subscription", back_populates="subscriber",
                                 foreign_keys="Subscription.subscriber_id")
    subscribers = relationship("Subscription", back_populates="target",
                               foreign_keys="Subscription.target_id")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")
    likes = relationship("Like", back_populates="comment")


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    post = relationship("Post", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    subscriber = relationship("User", back_populates="subscriptions",
                              foreign_keys=[subscriber_id])
    target = relationship("User", back_populates="subscribers",
                          foreign_keys=[target_id])

    __table_args__ = (
        UniqueConstraint("subscriber_id", "target_id", name="unique_subscription"),
    )
