from fastapi import APIRouter, Depends
from app.modules.maps.schemas import PlaceSearch, PlaceResponse
from app.modules.maps.service import maps_service

router = APIRouter()

@router.post("/search", response_model=list[PlaceResponse])
def search_places(search: PlaceSearch):
    return maps_service.search_places(search.query)
