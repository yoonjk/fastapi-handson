from fastapi import FastAPI
from fastapi import Request
from logger import logger 
from middleware import log_middleware
import time  
from starlette.middleware.base import BaseHTTPMiddleware 

app = FastAPI() 

app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch = log_middleware)

@app.get("/")
async def get_root() ->dict:
  return {"message": "Hello"}

@app.get("/items")
async def get_items():
  # logger.info("Request to index page")
  return {"message": "test"}