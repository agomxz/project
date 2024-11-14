from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Float,
)
from app.db.session import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String)
