from pydantic import BaseModel
from typing import Optional

class PlaceSearch(BaseModel):
    query: str
    location: Optional[str] = None
    radius: Optional[int] = None

class PlaceResponse(BaseModel):
    name: str
    address: str
    place_id: str
    location: dict
