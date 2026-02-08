from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    username : str
    email : str
    password: str
    
class UserResponseSchema(BaseModel):
    username : str
    email : str
