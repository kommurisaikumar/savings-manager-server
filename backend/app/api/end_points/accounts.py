from fastapi import Depends, APIRouter,FastAPI, HTTPException
from typing import List
from app import crud

from sqlalchemy.orm.session import Session
from app.api.deps import get_db
from app.schemas import Account, AccountCreate, AccountUpdate

router = APIRouter()

@router.get("/", response_model=List[Account])
async def get_accounts(user_id: int, db: Session = Depends(get_db)):
    db_accounts = crud.accounts.get_user_accounts(db, user_id)
    if not db_accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_accounts

@router.get("/{account_id}", response_model=Account)
async def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.accounts.get_account(db, account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.post("/", response_model=Account)
async def create_account(user_id: int, data: AccountCreate, db:Session = Depends(get_db)):
    db_account = crud.accounts.create_account(db, user_id, data)
    if not db_account:
        raise HTTPException(status_code=404, detail="Error while creating Account")
    return db_account

@router.put("/{account_id}", response_model=Account)
async def update_account(account_id: int, data: AccountUpdate, db:Session = Depends(get_db)):
    db_account = crud.accounts.update_account(db, account_id, data)
    if not db_account:
        raise HTTPException(status_code=404, detail="Error while updating Account")
    return db_account
