from fastapi import Depends, FastAPI

from app.bearer import get_current_user
from app.db.repository.user_repo import as_user
from app.db.tables.user_table import UserTable
from app.routes.auth import auth

app = FastAPI()

app.include_router(auth)

@app.get("/me")
def account(user: UserTable = Depends(get_current_user)):
    return as_user(user)
