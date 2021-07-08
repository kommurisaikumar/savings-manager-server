from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime, Enum
from app.db.base import Base

class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey('users.id'))
    amount = Column(Integer, nullable=False)
    note = Column(String(255))
    from_acc_id = Column(ForeignKey('accounts.id'))
    to_acc_id = Column(ForeignKey('accounts.id'))
    category_id = Column(ForeignKey('categories.id'))
    type = Column(Enum('Income', 'Expenditure', 'Move'), nullable=False)
    transaction_date = Column(DateTime, server_default=func.now(), nullable=False)
    created = Column(DateTime, server_default=func.current_timestamp(), nullable=True)
    modified = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.now())
    deleted = Column(DateTime, nullable=True)
