from pydantic import BaseModel
from typing import Optional

class CategorySingleIn (BaseModel):
    id: int
    user_id: int

class CategoryListIn (BaseModel):
    id: Optional[int]
    user_id: int

class Category (BaseModel):
    id: int
    name: str
    description: Optional[str]
    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str]

class CategoryUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]