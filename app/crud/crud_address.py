from datetime import datetime
from typing import Any, Dict

from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import Address
from app.schemas.user import AddressBase

logger = config.logger


def create(db: Session, obj_in: AddressBase) -> Dict[str, Any]:
    """
    Create Address
    - **obj_in**: Address object

    Returns:
        - **address**: Address object
    """
    try:
        date_created = datetime.now().strftime("%Y-%m-%d")

        logger.info(obj_in)

        db_obj = Address(
            street=obj_in.street,
            city=obj_in.city,
            state=obj_in.state,
            zip=obj_in.zip,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        result = {"email": obj_in.street, "created_at": date_created}

        return result
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to create address")
