from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    details: Optional[str] = None
    completed: bool
    date_created: str
