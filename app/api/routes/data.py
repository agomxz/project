from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api.deps import (
    SessionDep,
)
from app.core.config import settings
from app.models import (

    UserCreate,
    UserPublic,

)
from app.utils import generate_new_account_email, send_email

import json

router = APIRouter()

@router.post(
    "/",  
)
def load_data() -> Any:
    """
    Load data.json
    """

    return {}
