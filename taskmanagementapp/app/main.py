from fastapi import FastAPI
from app.modules.utils.db import Base, engine
from app.modules.tasks.routers import task_router as tasks_routes
from app.modules.user.routers import user_router as user_routes

from app.modules.tasks.models import TaskModel 
from app.modules.user.models import UserModel

Base.metadata.create_all(engine)

app = FastAPI(title="My FastAPI Application", description="A simple FastAPI application", version="1.0.0") 
app.include_router(tasks_routes)
app.include_router(user_routes)