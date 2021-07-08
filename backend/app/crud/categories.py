from sqlalchemy.orm import Session
from app import models, schemas
from fastapi.encoders import jsonable_encoder

class CRUDCategories:
    def get_user_categories(self, db: Session, user_id: int):
        return db.query(models.Categories).filter(models.Categories.user_id == user_id).all()

    def get_category(self, db: Session, category_id: int):
        return db.query(models.Categories).filter(models.Categories.id == category_id).first()
    
    def create_category(self, db: Session, user_id: int, data: schemas.CategoryCreate):
        db_category = models.Categories(**jsonable_encoder(data), user_id=user_id)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category if db_category else False
    
    def update_category(self, db: Session, t_id: int, data: schemas.CategoryUpdate):
        db_category = self.get_category(db, t_id)
        if db_category is None:
            return False
        else:
            update_data = data.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_category, field, update_data[field])
            db.commit()
            db.refresh(db_category)
            return db_category

categories = CRUDCategories()
