from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: str
    contact: Optional[str]
    created: datetime
    modified: datetime
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: str
    contact: Optional[str]


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    contact: Optional[str]
    class Config:
        orm_mode = True