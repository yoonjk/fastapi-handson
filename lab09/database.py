from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os    

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD") 
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = "mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}".format(DB_USERNAME=DB_USERNAME, DB_PASSWORD=DB_PASSWORD, DB_SERVER=DB_SERVER, DB_PORT=DB_PORT, DB_NAME=DB_NAME)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal() 
  
  try:
    yield db
  finally:
    db.close()