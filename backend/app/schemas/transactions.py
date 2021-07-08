from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    id: int
    amount: int
    note: Optional[str]=None
    from_acc_id: Optional[int]=None
    to_acc_id: Optional[int]=None
    type: str
    category_id: int
    class Config:
        orm_mode = True


class TransactionCreate(BaseModel):
    amount: int
    note: Optional[str]=None
    from_acc_id: Optional[int]=None
    to_acc_id: Optional[int]=None
    type: str
    category_id: int
    class Config:
        orm_mode = True


class TransactionUpdate(BaseModel):
    amount: Optional[int]
    note: Optional[str]
    from_acc_id: Optional[int]
    to_acc_id: Optional[int]
    type: Optional[str]
    category_id: Optional[int]
