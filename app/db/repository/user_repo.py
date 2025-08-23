import secrets

from sqlalchemy.orm import Session

from app.db.tables.secret_table import SecretTable
from app.db.tables.user_table import UserTable
from app.models.user import UserRegister, User

def get_user_by_mail(db: Session, mail: str):
    return db.query(UserTable).filter(UserTable.email.is_(mail)).first()

def register_user(db: Session,user_data : UserRegister):
    user = UserTable(email= user_data.mail, name=user_data.name, password=user_data.password)
    with db:
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def get_new_token_by_id(db: Session,user_id : int):
    token = secrets.token_urlsafe(32)
    secret = db.query(SecretTable).filter(SecretTable.user_id.is_(user_id)).first()
    if secret:
        secret.token = token
    else:
        secret = SecretTable(user_id=user_id, token=token)
        db.add(secret)
    db.commit()
    db.refresh(secret)
    return secret.token

def as_user(user: UserTable):
    return User(id=user.id, name=user.name, email=user.email)