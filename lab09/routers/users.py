from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from models import UserModel, Base
from routers import crud
from database import SessionLocal, engine, get_db

router = APIRouter()

Base.metadata.create_all(bind=engine)

db_conn = Annotated[Session, Depends(get_db)]    

@router.get("/users")
def read_user_all(db : db_conn):
    tasks = crud.get_user_all(db)
    
    return tasks

@router.get("/users/{user_id}")
def read_task(user_id: int, db: db_conn):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/")
def create_user(user: UserModel, db: db_conn):
    return crud.create_user(db, user)