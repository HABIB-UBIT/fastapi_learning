from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    return {"message": "Events Module"}
