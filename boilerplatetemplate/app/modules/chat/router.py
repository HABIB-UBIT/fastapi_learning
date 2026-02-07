from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_chat():
    return {"message": "Chat Module"}
