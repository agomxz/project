from datetime import datetime
from typing import Any, Dict

from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import Tasks, TaskAssigments, TaskNotes
from app.schemas.task import TaskBase
from sqlalchemy import delete

logger = config.logger


def create(db: Session, obj_in: TaskBase) -> Dict[str, Any]:
    """
    Create Task
    - **obj_in**: Task object

    Returns:
        - **task**: task object

    """
    try:
        date_created = datetime.now().strftime("%d/%m/%Y")

        db_obj = Tasks(
            title=obj_in.title,
            details=obj_in.details,
            completed=obj_in.completed,
            date_created=obj_in.date_created,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        result = {"title": obj_in.title, "created_at": date_created}

        return result
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to create task")


def get_by_id(db: Session, task_id: int):
    """
    Get Task By Id
    - **user_id**: User id

    Returns:
        - **user**: User object

    """
    try:
        user = db.query(Tasks).filter(Tasks.id == task_id).first()
        return user
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to get user by id")


def delete_notes(db: Session, user_id: int) -> Any:
    try:
        stmt = delete(TaskNotes).where(TaskNotes.user_id == user_id)
        db.execute(stmt)
        db.commit()
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to delete task notes")


def delete_assigments(db: Session, user_id: int) -> Any:
    try:
        stmt = delete(TaskAssigments).where(TaskAssigments.user_id == user_id)
        db.execute(stmt)
        db.commit()
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to delete task assigments")
