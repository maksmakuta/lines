from pydantic import BaseModel, EmailStr

from app.models.user import UserInfo

class UserLogin(BaseModel):
    username: str
    secret: str

class UserRegister(UserLogin):
    mail: EmailStr

class AuthResponse(BaseModel):
    user: UserInfo
    token: str