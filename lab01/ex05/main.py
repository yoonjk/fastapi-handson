from pydantic import BaseModel
from fastapi import FastAPI, Path

app = FastAPI() 

class Item(BaseModel):
  name: str
  description: str | None = None 
  price: float 
  tax: float 

class User(BaseModel):
  username: str
  full_name: str | None = None 

class Importance(BaseModel):
  importance: int
 
@app.put("/items/{item_id}")
async def update_item(
  *,
  item_id: int = Path(..., title="The ID of the item is get", gt=0, le=150),
  q: str | None = None,
  item: Item | None = None,
  user : User,
  importance : Importance
):
  results = {"item_id": item_id}
  
  if q:
    results.update({"q": q})
  
  if item:
    results.update({"item": item})
  
  if user:
    results.update({"user": user })  
   
  if importance:
    results.update({"importance": importance}) 
    
  return results