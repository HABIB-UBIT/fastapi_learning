from app.db.base import Base
from sqlalchemy import Column, Integer, String

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    # Add other fields as needed
