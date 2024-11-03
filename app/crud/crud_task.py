from datetime import datetime
from typing import Any, Dict

from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import User, TaskAssigments, TaskNotes

from app.schemas.user import UserCreate
from sqlalchemy import delete

logger = config.logger


def create_task(db: Session, obj_in: UserCreate) -> Dict[str, Any]:
    """
    Create Task
    - **obj_in**: Task object

    Returns:
        - **task**: task object

    """
    try:
        date_created = datetime.now().strftime("%Y-%m-%d")

        db_obj = User(
            user_name=obj_in.user_name,
            email=obj_in.email,
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            mobile=obj_in.mobile,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        result = {"email": obj_in.email, "created_at": date_created}

        return result
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to create user")


def get_by_id(db: Session, user_id: int):
    """
    Get Task By Id
    - **user_id**: User id

    Returns:
        - **user**: User object

    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
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
