from app.db.base import Base
from sqlalchemy import Column, Float, String, Date


class BondInstrument(Base):
    __tablename__ = "bond_instruments"

    isin = Column(String(12), primary_key=True)  # https://www.investopedia.com/terms/i/isin.asp
    name = Column(String(64))
    # amortization_info = relationship("AmortizationInfo")
    year_percent = Column(Float)
    maturity_date = Column(Date)
    face_value = Column(Float)
