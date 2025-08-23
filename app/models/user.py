from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

class UserRegister(BaseModel):
    name: str
    mail: str
    password: str

class UserLogin(BaseModel):
    mail: str
    password: str
