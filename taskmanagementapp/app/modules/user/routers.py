from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.modules.utils.settings import settings
from app.modules.utils.db import get_db
from app.modules.user import controllers
from app.modules.user.schema import UserResponseSchema, UserSchema

user_router = APIRouter(prefix=f"{settings.API_V1_STR}/users", tags=["users"])

@user_router.post("/register", response_model=UserResponseSchema,   summary="Register a new user", status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return controllers.register_user(body, db)