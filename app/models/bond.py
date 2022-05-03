from app.models.base import BaseModel
from sqlalchemy import Column, Float
from sqlalchemy.orm import relationship


class Bond(BaseModel):
    __tablename__ = "bonds"

    instrument = relationship("BondInstrument")
    yield_to_maturity = Column(Float)
    wallet = relationship("Wallet", back_populates="bonds")
    value = Column(Float)
