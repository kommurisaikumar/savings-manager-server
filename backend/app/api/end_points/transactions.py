from fastapi import Depends, APIRouter,FastAPI, HTTPException
from typing import List, Optional
from app import crud

from sqlalchemy.orm.session import Session
from app.api.deps import get_db
from app.schemas import Transaction, TransactionCreate, TransactionUpdate

router = APIRouter()


@router.get("/", response_model=List[Transaction])
def get_user_transactions(
    user_id: int,
    in_date: Optional[str] = None,
    in_month: Optional[str] = None,
    in_year: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    db: Session = Depends(get_db)):
    queryFilters = None
    if in_date or in_month or in_year or from_date or to_date:
        queryFilters = {
            "in_date": in_date,
            "in_month": in_month,
            "in_year": in_year,
            "from_date": from_date,
            "to_date": to_date
        }
    db_transactions = crud.transactions.get_user_transactions(db, user_id, queryFilters)
    if not db_transactions:
        raise HTTPException(status_code=404, detail="No transactions found")
    return db_transactions


@router.get("/{t_id}", response_model=Transaction)
def get_transaction(t_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.transactions.get_transaction(db, t_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.post("/", response_model=Transaction)
def create_transaction(user_id: int, data: TransactionCreate, db:Session = Depends(get_db)):
    db_transaction = crud.transactions.create_transaction(db, user_id, data)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Error while creating Transaction")
    return db_transaction

@router.put("/{t_id}", response_model=Transaction)
def update_transaction(t_id: int, data: TransactionUpdate, db:Session = Depends(get_db)):
    db_transaction = crud.transactions.update_transaction(db, t_id, data)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Error while updating Transaction")
    return db_transaction