from fastapi import FastAPI, Path, Query 

app = FastAPI() 

@app.get("/items_validation/{item_id}")
async def read_items_validation(
  *,
  item_id: int = Path(..., title="The ID of the item to get", qt=10, le=100),
  q: str = "hello",
  size: float = Query(..., gt=0, lt=7.75), 
  limit : int | None = None
):
  results = {"item_id": item_id}
  
  if q:
    results.update({"q": q})
    
  return results