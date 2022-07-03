from sqlalchemy import Column, String, ForeignKey, Float, DATETIME, TIMESTAMP

from app.db.base import BaseModel


class BondTransaction(BaseModel):
    __tablename__ = "bonds_transactions"

    security = None
    action = Column(String(16), ForeignKey('transaction_actions.name'))
    price = Column(Float)
    value = Column(Float)
    timestamp = Column(TIMESTAMP)
    fee = Column(Float)
