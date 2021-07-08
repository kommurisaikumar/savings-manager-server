from sqlalchemy.orm import Session
from app import models, schemas
from fastapi.encoders import jsonable_encoder

class CRUDAccounts:
    def get_user_accounts(self, db: Session, user_id: int):
        return db.query(models.Accounts).filter(models.Accounts.user_id == user_id).all()

    def get_account(self, db: Session, account_id: int):
        return db.query(models.Accounts).filter(models.Accounts.id == account_id).first()
    
    def create_account(self, db: Session, user_id: int, data: schemas.TransactionCreate):
        db_account = models.Accounts(**jsonable_encoder(data), user_id=user_id)
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account if db_account else False
    
    def update_account(self, db: Session, t_id: int, data: schemas.AccountUpdate):
        db_account = self.get_account(db, t_id)
        if db_account is None:
            return False
        else:
            update_data = data.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_account, field, update_data[field])
            db.commit()
            db.refresh(db_account)
            return db_account

accounts = CRUDAccounts()
