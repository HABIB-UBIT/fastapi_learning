from fastapi import APIRouter, status, Depends, Request
from sqlalchemy.orm import Session
from app.modules.utils.settings import settings
from app.modules.utils.db import get_db
from app.modules.user import controllers
from app.modules.user.schema import LoginSchema, UserResponseSchema, UserSchema

user_router = APIRouter(prefix=f"{settings.API_V1_STR}/users", tags=["users"])

@user_router.post("/register", response_model=UserResponseSchema,   summary="Register a new user", status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return controllers.register_user(body, db)


@user_router.post("/login", summary="Login an existing user", status_code=status.HTTP_200_OK)
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    return controllers.login_user(body, db)

@user_router.get("/is_auth", response_model=UserResponseSchema, summary="Get the authenticated user's information", status_code=status.HTTP_200_OK)
def is_authenticated(request: Request, db: Session = Depends(get_db)):
    return controllers.is_authenticated(request, db)