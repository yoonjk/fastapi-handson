from fastapi import FastAPI
from routers import todo 
app = FastAPI() 

app.include_router(todo.inventory_router)

 