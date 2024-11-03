from datetime import datetime
from typing import Any, Dict

from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import User
from app.schemas.user import UserCreate

logger = config.logger


def create_address(db: Session, obj_in: UserCreate) -> Dict[str, Any]:
    """
    Create Address
    - **obj_in**: Address object

    Returns:
        - **address**: Address object
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
        raise Exception("Failed to create address")
