from datetime import datetime
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import User, TaskNotes, TaskAssigments

from app.schemas.user import User as UserSchema
from app.schemas.user import UserCreate, UserUpdatePut, UserUpdatePatch
from sqlalchemy import delete

logger = config.logger


def create_user(db: Session, obj_in: UserCreate) -> Dict[str, Any]:
    """
    Create User
    - **obj_in**: User object

    Returns:
        - **user**: User object

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


def get_user_tasks(db: Session, user_id: int):
    try:
        query = (
            db.query(User, TaskNotes, TaskAssigments)
            .join(TaskNotes, TaskNotes.user_id == User.id)
            .join(TaskAssigments, TaskAssigments.user_id == User.id)
            .filter(User.id == user_id)
            .all()
        )

        notes_result = []
        assigments_result = []

        for user, notes, assigments in query:
            note = {
                "id": notes.id,
                "task_id": notes.task_id,
                "user_id": notes.user_id,
                "notes": notes.notes,
            }

            notes_result.append(note)

            assigment = {
                "id": assigments.id,
                "task_id": assigments.task_id,
                "user_id": assigments.user_id,
                "accepted": assigments.accepted,
            }

            assigments_result.append(assigment)

        result = {"task_notes": notes_result, "task_assigments": assigments_result}

        return result

    except Exception as e:
        logger.error(e)
        raise Exception("Failed to get tasks")


def get_by_id(db: Session, user_id: int):
    """
    Get User By Id

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


def get_by_email(db: Session, email: str) -> Optional[UserSchema]:
    """
    Get User By Email

    - **email**: User email

    Returns:
        - **user**: User object

    """
    try:
        user = db.query(User).filter(User.email == email).first()
        return user
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to get user by email")


def get_by_username(db: Session, username: str) -> Optional[UserSchema]:
    """
    Get User By Username

    - **username**: User username

    Returns:
        - **user**: User object
    """
    try:
        return db.query(User).filter(User.user_name == username).first()
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to get user by username")


def user_put(db: Session, user_id: int, user: UserUpdatePut) -> Any:
    """
    Update User

    - **user_id**: User id
    - **user**: User object

    Returns:
        - **user**: User object
    """
    try:
        db.query(User).filter(User.id == user_id).update(user.__dict__)
        db.commit()

        # Get updated user to return
        updated_user = db.query(User).filter(User.id == user_id).first()
        return updated_user
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to update user")


def user_patch(db: Session, user_id: int, user: UserUpdatePatch) -> Any:
    """
    Update User

    - **user_id**: User id
    - **user**: User object

    Returns:
        - **user**: User object
    """
    try:
        user_dict = user.__dict__
        data = {key: value for key, value in user_dict.items() if value is not None}

        db.query(User).filter(User.id == user_id).update(data)
        db.commit()

        # Get updated user to return
        updated_user = db.query(User).filter(User.id == user_id).first()
        return updated_user
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to update user")


def delete_user(
    db: Session,
    user_id: int,
) -> Any:
    try:
        stmt = delete(User).where(User.id == user_id)
        db.execute(stmt)
        db.commit()
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to delete user")
