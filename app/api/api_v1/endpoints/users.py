from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile
import io
import pandas as pd
from app.models.user_service import Transaction
from sqlalchemy.orm import Session
from datetime import datetime
from app.config import config
from app.db.session import get_db
from app.crud import crud_transaction
from pydantic import ValidationError

router = APIRouter()
logger = config.logger


@router.post("/load", status_code=status.HTTP_201_CREATED)
async def upload_csv(
    file: UploadFile = File(...), db: Session = Depends(get_db)
) -> Any:
    """
    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        Any: _description_
    """
    try:
        contents = await file.read()
        data = io.StringIO(contents.decode("utf-8"))

        df = pd.read_csv(data)

        data = df[["date", "transaction"]]
        date_format = "%m/%d/%Y"
        here = data.iterrows()

        list_transactions = []

        for index, row in here:
            print(index)
            print(row)
            new_date = datetime.strptime(row[0], date_format)

            type = "debit" if float(row[1]) < 0 else "credit"

            new_obj = Transaction(date=new_date, amount=float(row[1]), type=type)
            list_transactions.append(new_obj)

        return crud_transaction.create(db, list_transactions)

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {e}",
        )
    except HTTPException as e:
        logger.info(e)
        raise
    except Exception as e:
        logger.info(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while loading the file.",
        )


@router.get("/summary", status_code=status.HTTP_200_OK)
def get_summary(db: Session = Depends(get_db)) -> dict:
    summary = crud_transaction.get_summary(db)

    return {"credit": summary[0][0], "debit": summary[1][0]}
