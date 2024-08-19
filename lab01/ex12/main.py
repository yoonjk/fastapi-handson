from fastapi import (
  FastAPI, 
  HTTPException, 
  Request,
  status
  )
from pydantic import BaseModel 
from enum import Enum 

app = FastAPI() 

class Item(BaseModel):
  name: str 
  description: str | None = None 
  price: float 
  tax: float | None = None 
  tags: set[str] = set()
  
class Tags(Enum):
  items = "items"
  users = "users"
  
@app.post("/items", response_model=Item, 
          status_code = status.HTTP_201_CREATED, 
          tags=[Tags.items],
          summary="Create an Item",
          description="Create an item with all the information: "
          # "Name: description; price; tax; and a set of "
          # "unique tags",
          
          )
async def create_item(item: Item):
  """
  Create an item with all the information:
  
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
  """
  return item 

@app.get("/users", tags=[Tags.users])
async def read_users():
  return [{"username": "Kildong"}]