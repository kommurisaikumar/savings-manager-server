from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models, schemas
from typing import Dict
from fastapi.encoders import jsonable_encoder

class CRUDTransactions():
    def get_transaction(self, db: Session, tid: int):
        return db.query(models.Transactions).filter(models.Transactions.id == tid).first()

    def get_user_transactions(self, db: Session, user_id: int, filters: Dict):
        query = db.query(models.Transactions)
        result = None
        print("myresult", result)
        if filters: 
            if (filters["in_date"]):
                result = query.filter(
                    models.Transactions.user_id == user_id,
                    func.DATE(models.Transactions.created) == func.DATE(filters["in_date"])
                    ).all()
            elif (filters["in_month"]):
                result = query.filter(
                    models.Transactions.user_id == user_id,
                    func.MONTH(models.Transactions.created) == filters["in_month"],
                    func.YEAR(models.Transactions.created) == filters["in_year"]
                    ).all()
            elif (filters["in_year"]):
                result = query.filter(
                    models.Transactions.user_id == user_id,
                    func.YEAR(models.Transactions.created) == filters["in_year"]
                    ).all()
            elif (filters["from_date"]):
                result = query.filter(
                    models.Transactions.user_id == user_id,
                    func.DATE(models.Transactions.created) >= filters["from_date"]
                    ).all()
            elif (filters["to_date"]):
                result = query.filter(
                    models.Transactions.user_id == user_id,
                    func.DATE(models.Transactions.created) <= filters["to_date"]
                    ).all()
        else:
            result = query.filter(models.Transactions.user_id == 1).all()
        return result if result else False

    def create_transaction(self, db: Session, user_id: int, data: schemas.TransactionCreate):
        db_transaction = models.Transactions(**jsonable_encoder(data), user_id=user_id)
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction if db_transaction else False
    
    def update_transaction(self, db: Session, t_id: int, data: schemas.TransactionUpdate):
        db_transaction = self.get_transaction(db, t_id)
        if db_transaction is None:
            return False
        else:
            update_data = data.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_transaction, field, update_data[field])
            db.commit()
            db.refresh(db_transaction)
            return db_transaction

transactions = CRUDTransactions()