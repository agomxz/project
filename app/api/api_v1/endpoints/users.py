from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config import config
from app.db.session import get_db
from app.crud import crud_user
from app.crud import crud_task
from app.crud import crud_address

from pydantic import ValidationError
from app.schemas.user import UserCreate, UserUpdatePatch, UserUpdatePut

router = APIRouter()
logger = config.logger


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_obj: UserCreate, db: Session = Depends(get_db)) -> Any:
    """
    Create User

    - **new_user**: User object

    Returns:
        - **user**: User object
        - **400**: User (email, username, phone number) already exists
        - **400**: Invalid input
        - **500**: An error occurred while creating the user

    """
    try:
        user_exist = None
        user_exist = crud_user.get_by_email(db, user_obj.email)

        username_exists = None
        username_exists = crud_user.get_by_username(db, user_obj.user_name)

        mobile_exists = None
        mobile_exists = crud_user.get_by_mobile(db, user_obj.mobile)

        if user_exist:
            logger.warning("User already exists.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User email already exists.",
            )

        elif username_exists:
            logger.warning("Username already exists.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists.",
            )

        elif mobile_exists:
            logger.warning("Mobile already exists.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Mobile already exists.",
            )

        else:
            new_user = crud_user.create_user(db, user_obj)
            crud_address.create(db, user_obj.address)

            return new_user

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
        logger.error(f"Error creating user: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the user.",
        )


@router.get("/{user_id}", status_code=status.HTTP_201_CREATED)
def get_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    """
    Fetch User

    - **user_id**: int

    Returns:
        - **user**: User object
        - **500**: An error occurred while creating the user

    """
    try:
        user = crud_user.get_by_id(db, user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )

        user_dict = user.__dict__.copy()

        return user_dict

    except HTTPException as e:
        logger.warning(f"HTTPException: {e}")
        raise
    except Exception as e:
        logger.error(f"Error getting user by id: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while getting user by id.",
        )


@router.get("/user-tasks/{user_id}", status_code=status.HTTP_200_OK)
def user_tasks(user_id: int, db: Session = Depends(get_db)) -> Any:
    user = crud_user.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    data = crud_user.get_user_tasks(db, user_id)

    return data


@router.put("/{user_id}", status_code=status.HTTP_201_CREATED)
def put_user(
    user_id: int, user_obj: UserUpdatePut, db: Session = Depends(get_db)
) -> Any:
    """
    Update User
    - **new_user**: User object

    Returns:
        - **user**: User object
        - **400**: Invalid input
        - **500**: An error occurred while creating the user

    """
    try:
        if crud_user.get_by_id(db, user_id) is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )

        if crud_user.get_by_email(db, user_obj.email) is not None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Email already exists."
            )

        return crud_user.user_put(db, user_id, user_obj)

    except HTTPException as e:
        logger.warning(f"HTTPException: {e}")
        raise

    except Exception as e:
        logger.error(f"Error updating user: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurred while updating user.",
        )


@router.patch("/{user_id}", status_code=status.HTTP_201_CREATED)
def patch_user(
    user_id: int, user_obj: UserUpdatePatch, db: Session = Depends(get_db)
) -> Any:
    """
    Update User

    - **new_user**: User object

    Returns:
        - **user**: User object
        - **400**: Invalid input
        - **500**: An error occurred while creating the user

    """
    try:
        if crud_user.get_by_id(db, user_id) is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )

        if crud_user.get_by_email(db, user_obj.email) is not None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Email already exists."
            )

        return crud_user.user_patch(db, user_id, user_obj)

    except HTTPException as e:
        logger.warning(f"HTTPException: {e}")
        raise

    except Exception as e:
        logger.error(f"Error updating user: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurred while updating user.",
        )


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    """
    Delete User

    - **user_id**: int

    Returns:
        - **user**: User object
        - **500**: An error occurred while deleting the user
    """
    try:
        crud_task.delete_assigments(db, user_id)
        crud_task.delete_notes(db, user_id)
        crud_user.delete_user(db, user_id)
        return {"user_id": user_id}

    except HTTPException as e:
        logger.warning(f"HTTPException: {e}")
        raise
    except Exception as e:
        logger.error(f"Error deleteing user: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the user.",
        )
