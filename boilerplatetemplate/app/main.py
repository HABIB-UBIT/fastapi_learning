from fastapi import FastAPI
from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.events.router import router as events_router
from app.modules.chat.router import router as chat_router
from app.modules.maps.router import router as maps_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(events_router, prefix=f"{settings.API_V1_STR}/events", tags=["events"])
app.include_router(chat_router, prefix=f"{settings.API_V1_STR}/chat", tags=["chat"])
app.include_router(maps_router, prefix=f"{settings.API_V1_STR}/maps", tags=["maps"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Juno Backend"}
