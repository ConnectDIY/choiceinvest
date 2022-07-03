from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    name: Optional[str] = None
    # email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    # is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    name: str
    # email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    name: Optional[str]
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
