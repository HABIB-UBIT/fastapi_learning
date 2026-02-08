from typing import Optional
from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str = None
    is_completed: bool = False
    

class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool 