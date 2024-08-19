from fastapi import FastAPI, Body 
from pydantic import BaseModel, Field 

app = FastAPI() 

class Image(BaseModel):
  url : str 
  name: str

class Item(BaseModel):
  name: str 
  description: str | None = Field(
    None, title="The description of the item", max_length=300
  )
  price: float = Field(..., gt=0, description="The price must be greater than zero.")
  tax: float | None = None 
  tags: set[str] = []
  image: Image | None = None 

class Offer(BaseModel):
  name: str 
  description : str 
  price: float 
  items: list[Item]
  
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
  results = {"item_id": item_id, "item": item}
  
  return results

@app.post("/items")
async def create_offer(offer: Offer = Body(..., embed=True)):
  return offer 

@app.post("/items/multiple")
async def create_multiple_images(images : list[Image]):
  return images 

