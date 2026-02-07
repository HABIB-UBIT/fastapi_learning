from pydantic import BaseModel
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None

class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        from_attributes = True
