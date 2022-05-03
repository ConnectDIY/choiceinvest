from app.models.base import BaseModel
from sqlalchemy import Column, Float, String, Date
from sqlalchemy.orm import relationship


class BondInstrument(BaseModel):
    __tablename__ = "bond_instruments"

    name = Column(String(64))
    isin = Column(String(12))  # https://www.investopedia.com/terms/i/isin.asp
    # amortization_info = relationship("AmortizationInfo")
    year_percent = Column(Float)
    maturity_date = Column(Date)
