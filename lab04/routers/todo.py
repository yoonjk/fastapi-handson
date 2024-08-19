# todo
from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict: 
  todo_list.append(todo)
  
  return {"message" : "todo가 등록되었습니다."}

@todo_router.get("/todo")
async def retrieve_todo_all() -> dict:  
  return {"todos" : todo_list}

@todo_router.get("/todo/{todo_id}")
async def retrieve_todo(todo_id: int):
  for todo in todo_list:
    if todo["id"] == todo_id:
      return todo
  
  return {"message" : "id가 {0}인 todo가 존재하지 않습니다.".format(todo_id)}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
  for index in range(len(todo_list)):
    todo = todo_list[index]
    if todo["id"] == todo_id:
      todo_list.pop(index)
      
      return todo
  
  return {"message" : "id가 {0}인 todo가 존재하지 않습니다.".format(todo_id)}

@todo_router.delete("/todo")
async def delete_todo_all():
  todo_list.clear()
  
  return { "message" : "Todos가 삭제되었습니다."}