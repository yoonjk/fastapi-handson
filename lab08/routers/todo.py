from fastapi import APIRouter, Path, Query, HTTPException, status
from models import Item
inventory_router = APIRouter()

inventory = {
  1 : {
    "name" : "Milk",
    "price" : 3.99,
    "brand" : "Regular"
  }
}

@inventory_router.get("/items/{item_id}")
async def read_item(item_id: int=Path(description="The ID of the item you'd like to ", gt=0)):
  return inventory[item_id]

@inventory_router.post("/items")
async def add_item(item: Item):
  if item.id in inventory:
    return {"Error" : "Item Id already exists"}  
  inventory[item.id] = {"name" : item.name, "price": item.price, "brand": item.brand}
  
  return inventory

@inventory_router.get("/items")
async def read_item_all():
  return inventory

@inventory_router.get("/items/get-by-name")
async def get_by_name(name: str|None = None):
  print(name)
  for item_id in inventory:
    if inventory[item_id].name == name:
      return inventory[item_id] 
    
  return {"Data" : "Not found"}

@inventory_router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
  if item_id not in inventory:
    return {"Error" : "Item ID does not exists"}
  
  if item.name != None:
    inventory[item_id].name = item.name
  if item.price != None:
    inventory[item_id].price = item.price
 
  if item.brand != None:
    inventory[item_id].brand = item.brand
  
  return inventory[item_id]

  
@inventory_router.delete("/items/{item_id}")
async def delete_item(item_id: int):
  if item_id not in inventory:
    HTTPException(status_code=404, detail="Item ID does not exist.")
    
  del inventory[item_id]
  return {"Success": "Item deleted"}