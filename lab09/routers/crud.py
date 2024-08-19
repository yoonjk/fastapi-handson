from sqlalchemy.orm import Session
from models import User, UserModel

def get_user_all(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserModel):
    db_user= User(username=user.username, nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user