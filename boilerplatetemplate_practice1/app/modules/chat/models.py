from app.db.base import Base
from sqlalchemy import Column, Integer, String

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    # Add other fields as needed
