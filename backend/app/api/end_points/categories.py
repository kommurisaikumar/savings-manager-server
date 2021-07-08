from fastapi import Depends, APIRouter,FastAPI, HTTPException
from typing import List, Optional
from app import crud

from sqlalchemy.orm.session import Session
from app.api.deps import get_db
from app.schemas import Category, CategoryCreate, CategoryUpdate

router = APIRouter()

@router.get("/", response_model=List[Category])
async def get_accounts(user_id: int, db: Session = Depends(get_db)):
    db_accounts = crud.categories.get_user_categories(db, user_id)
    if not db_accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_accounts

@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.categories.get_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/", response_model=Category)
def create_category(user_id: int, data: CategoryCreate, db:Session = Depends(get_db)):
    db_category = crud.categories.create_category(db, user_id, data)
    if not db_category:
        raise HTTPException(status_code=404, detail="Error while creating category")
    return db_category

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, data: CategoryUpdate, db:Session = Depends(get_db)):
    db_category = crud.categories.update_category(db, category_id, data)
    if not db_category:
        raise HTTPException(status_code=404, detail="Error while updating category")
    return db_category