from datetime import datetime
from typing import Any, Dict
from typing import Union
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.config import config
from app.models.user_service import Transaction

logger = config.logger


def create(db: Session, obj_in: Union[Transaction]) -> Dict[str, Any]:
    """
    Create Data
    - **obj_in**: Transacction object list

    Returns:
        - **dict**: {}
    """
    try:
        db.add_all(obj_in)
        db.commit()
        return {"created_at": datetime.now().strftime("%Y-%m-%d")}
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to create data")


def get_summary(db: Session) -> Any:
    """
    Fetch summary
    - **obj_in**:

    Returns:
        - **dict**: {}
    """
    try:
        stmt = select(func.sum(Transaction.amount), Transaction.type).group_by(
            Transaction.type
        )

        result = db.execute(stmt).all()
        return result
    except Exception as e:
        logger.error(e)
        raise Exception("Failed to fetch data")
