from sqlalchemy import Column, Boolean, Integer, String, Text, DateTime, ForeignKey
from app.modules.utils.db import Base

class TaskModel(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    is_completed = Column(Boolean , default=False)