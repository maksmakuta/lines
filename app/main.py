from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.db import get_db
from app.db.repository.user_repo import get_user_by_mail, register_user, get_token_by_id, get_new_token_by_id
from app.models.user import UserRegister, UserLogin

app = FastAPI()

@app.post("/auth/register")
def register(user_data: UserRegister,db: Session = Depends(get_db)):
    user = get_user_by_mail(db,user_data.mail)
    if user:
        user = register_user(db, user_data)
        token = get_token_by_id(db, user.id)
        return {"user": user, "token": token}
    else:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email is already registered"
        )

@app.post("/auth/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_mail(db, user_data.mail)
    if user:
        token = get_new_token_by_id(db, user.id)
        return {"user": user, "token": token}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email is not registered"
        )