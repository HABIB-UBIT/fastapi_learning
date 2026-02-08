from app.modules.user.models import UserModel
from app.modules.user.schema import UserSchema, LoginSchema
from app.modules.utils.settings import settings
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Request
from datetime import datetime, timedelta
from pwdlib import PasswordHash
import jwt


password_hash= PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)


def register_user(body: UserSchema, db:Session):
    is_user= db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    is_user= db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email address already exists")
    hashed_password= get_password_hash(body.password)
    new_user= UserModel(username= body.username, email= body.email, hashed_password= hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body: LoginSchema, db:Session):
    is_user= db.query(UserModel).filter(UserModel.email == body.email).first()
    if not is_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    if not password_hash.verify(body.password, is_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    # exp_time= datetime.now() + timedelta(minutes=settings.EXP_TIME)
    exp_time= datetime.now() + timedelta(seconds=5)
    
    token= jwt.encode({"user_id": is_user.id, "exp": exp_time}, settings.SECRET_KEY, settings.ALGORITHM)

    return {"token": token}


def is_authenticated(request:Request, db:Session):
   token= request.headers.get("Authorization")
   if not token:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")
   
   token= token.split(" ")[-1]
   data= jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
#    print(data)
   user_id= data.get("user_id") 
   exp_time= int(data.get("exp"))
   print("the exp time is", exp_time)
   current_time= datetime.now().timestamp()
   print("the current time is", current_time)
   print("the time is", exp_time - current_time)
   if current_time > exp_time:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
   
   is_user= db.query(UserModel).filter(UserModel.id == user_id).first()
   if not is_user:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
   
   return is_user