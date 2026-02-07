from pydantic import BaseModel

## productDTO inherting from BaseModel
class productDTO(BaseModel):  
    id: int
    title: str
    price: float =0.00
    quantity: int =0