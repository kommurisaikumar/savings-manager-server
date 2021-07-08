from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas import User, UserUpdate
from app import crud

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users(db: Session = Depends(get_db)):
    return crud.users.get_all_users(db)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user =  crud.users.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    print(db_user)
    return db_user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, data: UserUpdate, db:Session = Depends(get_db)):
    db_transaction = crud.users.update_user(db, user_id, data)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Error while updating user")
    return db_transaction