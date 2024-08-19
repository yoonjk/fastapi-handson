from sqlalchemy import Column, Integer, String
from database import Base 
from pydantic import BaseModel

class User(Base):
  __tablename__ = "user_01"
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), index=True)
  nickname = Column(String(100))
  
class UserModel(BaseModel):
  username: str
  nickname: str

