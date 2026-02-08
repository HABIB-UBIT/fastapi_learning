from app.modules.user.models import UserModel
from app.modules.user.schema import UserSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from pwdlib import PasswordHash

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