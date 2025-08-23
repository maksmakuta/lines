from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.tables.secret_table import SecretTable
from app.db.tables.user_table import UserTable

security = HTTPBearer()

def get_current_user(
        creds: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = creds.credentials
    secret = db.query(SecretTable).filter(SecretTable.token.is_(token)).first()
    if not secret:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(UserTable).filter(UserTable.id.is_(secret.user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
