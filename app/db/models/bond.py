from app.db.base import BaseModel
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Bond(BaseModel):
    __tablename__ = "bonds"

    instrument = Column(String(12), ForeignKey("bond_instruments.isin"))
    yield_to_maturity = Column(Float)
    # wallet = relationship("Wallet", back_populates="bonds")
    value = Column(Float)
