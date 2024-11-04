from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    user_name: str
    email: EmailStr
    first_name: str
    last_name: str
    mobile: str


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip: str


class UserCreate(UserBase):
    address: AddressBase


class Address(UserBase):
    address_id: int


class User(UserBase):
    user_id: int


class UserUpdatePut(BaseModel):
    email: EmailStr
    user_name: str
    first_name: str
    last_name: str
    mobile: str


class UserUpdatePatch(BaseModel):
    email: Optional[EmailStr | None]
    user_name: Optional[str | None]
    first_name: Optional[str | None]
    last_name: Optional[str | None]
    mobile: Optional[str | None]
