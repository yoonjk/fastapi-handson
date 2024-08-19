from fastapi import FastAPI, Query
from pydantic import BaseModel 

app = FastAPI() 

tax = {"tax": 0}

class Item(BaseModel):
  name: str 
  description: str | None = None 
  price : float 
  tax: float | None = None 
  
@app.post("/items")
async def create_item(item: Item):
  item_dict = item.dict()
 
    
  if item.tax:
    price_with_tax = tax['tax'] + item.price + item.tax 
    tax['tax'] = price_with_tax
    item_dict.update({"price_with_tax": price_with_tax})
    
  return item_dict 


@app.put("/items/{item-id}")
async def create_item_with_put(item_id : int , item: Item, q : str | None = None):
  result =  {"item_id": item_id , **item.dict()}
  
  if q:
    result.update({"q": q})
    
  return result

@app.get("/items")
async def read_items(q:str |None = Query("fixedquery", min_length=3, max_length=10, regex="^fixedquery")):
  results = {"items" : [{"items" : "Foo"}, {"item_id": "Bar"}]}
  
  if q:
    results.update({"q": q})
    
  return results

@app.get("/items/hidden")
async def hidden_query(hidden_query: str | None = Query(None, include_in_schema=False)):
  if hidden_query:
    return {"hidden_query": hidden_query}
  
  return {"hidden_query": "Not found"}