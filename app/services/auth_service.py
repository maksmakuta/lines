import secrets
import hashlib

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.tables import User
from app.models.auth import UserRegister, UserLogin, AuthResponse
from app.services.models_services import to_user_info


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(db: Session, reg_data: UserRegister):
    user = User(username=reg_data.username, mail=reg_data.mail ,password=hash_password(reg_data.secret))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, log_data: UserLogin):
    user = db.query(User).filter(User.username == log_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Username not found"
        )
    if user.password != hash_password(log_data.secret):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password is wrong"
        )
    token = secrets.token_hex(32)
    user.token = token
    db.commit()
    db.refresh(user)
    return AuthResponse(
        user=to_user_info(db,user),
        token= token
    )

def get_user_by_token(db: Session, token: str):
    return db.query(User).filter(User.token == token).first()


def get_user_by_mail(db: Session, mail: str):
    return db.query(User).filter(User.mail == mail).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
