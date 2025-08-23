from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.bearer import get_current_user
from app.db.db import get_db
from app.db.repository.user_repo import get_user_by_mail, register_user, get_new_token_by_id, as_user
from app.db.tables.user_table import UserTable
from app.models.user import UserRegister, UserLogin

app = FastAPI()

@app.post("/auth/register")
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


@app.post("/auth/login")
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

@app.get("/me")
def account(user: UserTable = Depends(get_current_user)):
    return as_user(user)
