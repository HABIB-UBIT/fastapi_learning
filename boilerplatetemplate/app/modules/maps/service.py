import googlemaps
from app.core.config import settings

class MapsService:
    def __init__(self):
        self.client = None
        if settings.GOOGLE_MAPS_API_KEY:
            self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def search_places(self, query: str):
        if not self.client:
            return {"error": "Google Maps API key not configured"}
        # Placeholder for actual implementation
        return [{"name": "Test Place", "address": "123 Test St", "place_id": "123", "location": {"lat": 0, "lng": 0}}]

maps_service = MapsService()
