from sqlalchemy import Boolean, Column, Integer,  String, func, DateTime
from app.db.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(255), unique=True)
    contact = Column(String(20), unique=True)
    password = Column(String(20))
    is_active = Column(Boolean, server_default='1')
    created = Column(DateTime, server_default=func.current_timestamp(), nullable=True)
    modified = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.now())
