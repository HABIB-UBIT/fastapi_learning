from app.modules.tasks.schema import TaskSchema
from sqlalchemy.orm import Session
from app.modules.tasks.models import TaskModel
from fastapi import HTTPException, status

def create_task(body:TaskSchema, db: Session):
    data= body.model_dump()
    new_task = TaskModel(**data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task

def get_all_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks

def get_task_by_id(task_id: int, db: Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

def update_task(task_id: int, body: TaskSchema, db: Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    for key, value in body.model_dump().items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    
    return task


def delete_task(task_id: int, db:Session):
    task= db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return None