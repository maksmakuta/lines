from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.db import get_db
from app.db.repository.user_repo import get_user_by_mail, register_user, get_new_token_by_id, as_user
from app.models.user import UserRegister, UserLogin

auth = APIRouter(prefix="/auth", tags=["auth"])

@auth.post("/register")
def register(user_data: UserRegister,db: Session = Depends(get_db)):
    user = get_user_by_mail(db,user_data.mail)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered"
        )
    else:
        user = register_user(db, user_data)
        token = get_new_token_by_id(db, user.id)
        return {"user": as_user(user), "token": token}


@auth.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_mail(db, user_data.mail)
    if user:
        token = get_new_token_by_id(db, user.id)
        return {"user": as_user(user), "token": token}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email is not registered"
        )