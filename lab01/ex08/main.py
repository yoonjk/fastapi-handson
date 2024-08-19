from fastapi import FastAPI, Body, Cookie, Header
from pydantic import BaseModel, Field 

app = FastAPI() 

class Item(BaseModel):
  name: str = Field(..., example="Foo")
  description: str | None = Field(
    None, title="The description of the item", max_length=300, example="A very nice Item"
  )
  price: float = Field(..., gt=0, description="The price must be greater than zero.", example=10.25)
  tax: float | None = Field(None, example=0.5)
  
  
## Part 12 - Cooke and Header Parameters
@app.get("/items")

async def read_items(
  cookie_id : str | None = Cookie(None),
  accept_encoding: str | None = Header(None, convert_underscores=False),
  sec_ch_ua: str | None = Header(None),
  user_agent: str | None = Header(None),
  x_token: list[str] | None = Header(None)
):
  return {
    "cookie_id": cookie_id,
    "Accept-Encoding": accept_encoding,
    "sec-ch-ua": sec_ch_ua,
    "User-Agent": user_agent,
    "X-Token values": x_token
  }
  
