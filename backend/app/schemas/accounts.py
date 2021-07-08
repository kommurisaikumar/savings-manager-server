from pydantic import BaseModel
from typing import Optional

class AccountSingle (BaseModel):
    id: int
    user_id: int

class AccountList (BaseModel):
    id: Optional[int]
    user_id: int

class Account(BaseModel):
    id: int
    name: str
    description: Optional[str]
    class Config:
        orm_mode = True

class AccountCreate(BaseModel):
    name: str
    description: str

class AccountUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]