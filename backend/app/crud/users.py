from sqlalchemy.orm import Session
from app import models, schemas

class CRUDUsers():
    def get_all_users(self, db: Session):
        return db.query(models.Users).all()

    def get_user(self, db: Session, user_id: int):
        return db.query(models.Users).filter(models.Users.id == user_id).first()
    
    def update_user(self, db:Session, user_id: int, data: schemas.UserUpdate):
        db_user = self.get_user(db, user_id)
        if db_user is None:
            return False
        else:
            update_data = data.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_user, field, update_data[field])
            db.commit()
            db.refresh(db_user)
            return db_user

users = CRUDUsers()
