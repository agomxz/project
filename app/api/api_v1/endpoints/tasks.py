from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config import config
from app.db.session import get_db
from app.crud import crud_task

from pydantic import ValidationError
from app.schemas.task import TaskBase

router = APIRouter()
logger = config.logger


@router.post("/task/", status_code=status.HTTP_201_CREATED)
def create_users(task_obj: TaskBase, db: Session = Depends(get_db)) -> Any:
    """
    Create Task

    - **task_obj**: TaskBase object

    Returns:
        - **user**: Task object
        - **400**: User (email) already exists
        - **400**: Invalid input
        - **500**: An error occurred while creating the user

    """
    try:
        return crud_task.create(db, task_obj)

    except ValidationError as e:
        logger.error(f"Invalid input: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {e}",
        )
    except HTTPException as e:
        logger.warning(f"HTTPException: {e}")
        raise
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the task.",
        )
