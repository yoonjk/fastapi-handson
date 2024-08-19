from fastapi import FastAPI, Form, Body 
from pydantic import BaseModel 

app = FastAPI() 
class User(BaseModel):
  username: str 
  password: str 
  
@app.post("/lgoin")
async def login(username: str = Form(...), password: str = Form(...)):
  print('password;', password)
  
  return {"username": username}
  
@app.post("/login-json")
async def login_json(user: User):
  return user 

@app.post("/login-body")
async def login_json(username: str = Body(...), password: str = Body(...)):
  return {"username": username}