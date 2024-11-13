import datetime
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID


from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Float,
    String,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def _get_date():
    date = datetime.datetime.now(datetime.timezone.utc)
    return date.strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=True, unique=True, index=True)
    created_at = Column(DateTime, default=_get_date)
    first_name = Column(String)
    last_name = Column(String)
    mobile = Column(String, unique=True)
    address_id = Column(Integer, ForeignKey("address.id"), unique=True, index=True)


@dataclass
class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)


@dataclass
class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String)


@dataclass
class Tasks(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    details = Column(String, nullable=True)
    completed = Column(Boolean)
    priority = Column(String, nullable=True)
    date_created = Column(String, nullable=True)


@dataclass
class TaskAssigments(Base):
    __tablename__ = "task_assignments"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    task_id = Column(Integer)
    user_id = Column(Integer)
    accepted = Column(Boolean)


@dataclass
class TaskNotes(Base):
    __tablename__ = "task_notes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    task_id = Column(Integer)
    user_id = Column(Integer)
    notes = Column(String)
