from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime, Enum
from app.db.base import Base

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey('users.id'))
    name = Column(String(40), nullable=False)
    description = Column(String(255))
    created = Column(DateTime, server_default=func.current_timestamp(), nullable=True)
    modified = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.now())
    deleted = Column(DateTime, nullable=True)
