from pydantic import BaseModel
from typing import List

class Item(BaseModel):
  id: int
  item : str

  
class Items(BaseModel):
  todos : List[Item]
  