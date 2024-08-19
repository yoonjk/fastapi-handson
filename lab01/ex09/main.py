from fastapi import FastAPI, status 

app = FastAPI() 

@app.post("/items", status_code = status.HTTP_201_CREATED)
async def create_item(name: str):
  return {"name": name}

@app.delete("/items/{item_i}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_item(item_id : int):
  return {"item_id": item_id}

@app.get("/items/{item_id}", status_code = status.HTTP_302_FOUND)
async def read_item_redirect(item_id : int):
  return {"item_id": item_id}