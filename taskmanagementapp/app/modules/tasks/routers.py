from fastapi import APIRouter, HTTPException, Depends, status
from app.modules.utils.db import get_db
from typing import List
from app.modules.utils.settings import settings
from app.modules.tasks import controllers
from app.modules.tasks.schema import TaskSchema, TaskResponseSchema
from sqlalchemy.orm import Session

task_router = APIRouter(prefix=f"{settings.API_V1_STR}/tasks", tags=["tasks"])


@task_router.post("/create", response_model=TaskResponseSchema, summary="Create a new task", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controllers.create_task(body, db)

@task_router.get("/get_tasks",response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db)):
    return controllers.get_all_tasks(db)

@task_router.get("/get_task/{task_id}", response_model=TaskResponseSchema, summary="Get a task by ID", status_code= status.HTTP_200_OK)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    return controllers.get_task_by_id(task_id, db)

@task_router.put("/update_task/{task_id}", response_model=TaskResponseSchema, summary="Update a task by ID", status_code=status.HTTP_201_CREATED)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controllers.update_task(task_id, body, db)

@task_router.delete("/delete_task/{task_id}", summary="Delete a task by ID", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controllers.delete_task(task_id, db)




