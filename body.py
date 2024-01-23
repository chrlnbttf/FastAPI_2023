from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

api = FastAPI(title = 'My API')

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None

@api.post('/item')
def post_item(item: Item):
    return {
        'itemid' = item.itemid
    }