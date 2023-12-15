from typing import Optional

from pydantic import ConfigDict, BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: bool = False
    is_enabled: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


# Additional properties stored in DB but not returned by API
class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
class User(UserInDBBase):
    ...
