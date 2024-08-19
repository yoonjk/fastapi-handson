from fastapi import (
  FastAPI, 
  HTTPException, 
  Request
  )
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI() 

class UnicornException(Exception):
  def __init__(self, name: str):
    self.name = name 

@app.get("/validation_item/{item_id}")
async def read_validation_items(item_id: int):
  if item_id == 3:
    raise HTTPException(status_code = 418, detail="Nope! I don't like 3.*")
  
  return {"item_id": item_id}


@app.exception_handler(UnicornException)
async def uvicorn_exception_handler(request: Request, exc: UnicornException):
  return JSONResponse (
    status_code = 418,
    content = {"message": f"Opps! {exc.name} did something. There goes a rainbow..."}
  )

@app.get("/unicorns/{name}")
async def read_uvicorns(name: str):
  if name == 'pole':
    raise UnicornException(name = name)
  
  return {"uvicorn_name": name}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
  return PlainTextResponse(str(exc), status_code=400)


@app.get("/validation_items/{item_id}")
async def read_validation_items(item_id: int):
  if item_id == 3:
    raise HTTPException(status_code = 418, detail="Nope! I dont' like 3.")
  
  return {"item_id": item_id}