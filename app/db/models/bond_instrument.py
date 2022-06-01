from app.db.base import BaseModel
from sqlalchemy import Column, Float, String, Date


class BondInstrument(BaseModel):
    __tablename__ = "bond_instruments"

    name = Column(String(64))
    isin = Column(String(12))  # https://www.investopedia.com/terms/i/isin.asp
    # amortization_info = relationship("AmortizationInfo")
    year_percent = Column(Float)
    maturity_date = Column(Date)
    face_value = Column(Float)
