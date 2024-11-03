import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base


def _get_date():
    date = datetime.datetime.now(datetime.timezone.utc)
    return date.strftime("%Y-%m-%d %H:%M:%S")


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


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)

    # user = relationship("User", back_populates="address")


class Tasks(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    details = Column(String, nullable=True)
    completed = Column(Boolean)
    priority = Column(String, nullable=True)
    date_created = Column(String, nullable=True)


class TaskAssigments(Base):
    __tablename__ = "task_assignments"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    accepted = Column(Boolean)


class TaskNotes(Base):
    __tablename__ = "task_notes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    notes = Column(String)
