from app.db.base import BaseModel
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Bond(BaseModel):
    __tablename__ = "bonds"

    instrument = Column(String(12), ForeignKey("bond_instruments.isin"))
    wallet_id = Column(Integer, ForeignKey("wallets.id"))
    value = Column(Float)
