from app.db.base import Base
from sqlalchemy import Column, String


class TransactionAction(Base):
    __tablename__ = "transaction_actions"

    name = Column(String(16), primary_key=True)
