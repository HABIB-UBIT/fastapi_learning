from pydantic import BaseModel

class ChatCreate(BaseModel):
    participant_id: int

class ChatResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True
