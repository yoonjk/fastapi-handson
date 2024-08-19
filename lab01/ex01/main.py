from fastapi import FastAPI 
from enum import Enum 

app = FastAPI()

class FoodEnum(str, Enum):
  fruits = "fruites"
  vegetables = "vegetables"
  dairy = "dairy"
  

@app.get("/")
async def root():
  return {"message": "hello world"}

@app.post("/")
async def post():
  return {"message": "hello from the post route"}

@app.put("/")
async def put():
  return {"message": "hello from the put route"}

@app.delete("/")
async def delete():
  return {"message" : "hello from the delete route"}

@app.get("/items")
async def list_items():
  return {"message": "list items route"}

@app.get("/items/{item_id}")
async def get_items(item_id: int):
  return {"item": item_id}

@app.get("/users")
async def list_users():
  return {"message": "list users route"}

@app.get("/users/{user_id}")
async def get_users(user_id: str):
  return {"user_id is ": user_id}

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
  if food_name == FoodEnum.vegetables:
    return {
      "food_name" : food_name,
      "message" : "you are healthy"
    } 

  if food_name == FoodEnum.fruits:
    return {
      "food_name" : food_name,
      "message" : "you are still healthy, but like sweet things"
    }
  return {"food_name" : food_name, "message" : "I like chocolate milk"}