from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.db.db import get_db
from app.models.auth import UserRegister, UserLogin, AuthResponse
from app.models.user import UserInfo
from app.services.auth_service import get_user_by_mail, register_user, login_user
from app.services.models_services import to_user_info

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register", response_model=UserInfo)
def register(reg_data: UserRegister, db: Session = Depends(get_db)):
    user = get_user_by_mail(db,str(reg_data.mail))
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is used"
        )
    else:
        user = register_user(db,reg_data)
        return to_user_info(db,user)

@auth_router.post("/login", response_model=AuthResponse)
def login(log_data: UserLogin, db: Session = Depends(get_db)):
    return login_user(db,log_data)
