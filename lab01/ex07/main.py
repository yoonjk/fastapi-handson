from fastapi import FastAPI, Body 
from pydantic import BaseModel, Field 

app = FastAPI() 

class Item(BaseModel):
  name: str = Field(..., example="Foo")
  description: str | None = Field(
    None, title="The description of the item", max_length=300, example="A very nice Item"
  )
  price: float = Field(..., gt=0, description="The price must be greater than zero.", example=10.25)
  tax: float | None = Field(None, example=0.5)
  
  # class Config:
  #   json_schema_extra = {
  #     "example": {
  #       "name": "Foo",
  #       "description" : "A very nice Item",
  #       "price": 10.25,
  #       "tax": 0.25
  #     }
  #   }

# declare-request-example-data

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
  results = {"item_id": item_id, "item": item}
  
  return results

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]