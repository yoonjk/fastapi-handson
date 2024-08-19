from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
  id: int
  name: str
  price: int 
  brand: Optional[str] = None
  

  

  