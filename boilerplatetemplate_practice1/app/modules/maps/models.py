from app.db.base import Base
from sqlalchemy import Column, Integer, String

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, unique=True, index=True)
    name = Column(String)
    address = Column(String)
