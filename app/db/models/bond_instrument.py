from app.db.base import Base
from sqlalchemy import Column, Float, String, Date, ForeignKey, Integer


class BondInstrument(Base):
    __tablename__ = "bond_instruments"

    isin = Column(String(12), primary_key=True)  # https://www.investopedia.com/terms/i/isin.asp
    name = Column(String(64))
    amortization_info = Column(Integer, ForeignKey("amortization_info.id"))
    interest = Column(Float)
    interest_type = Column(String(32), ForeignKey("interest_types.name"))
    maturity_date = Column(Date)
    face_value = Column(Float)
    yield_to_maturity = Column(Float)
    category = Column(String(32), ForeignKey("bond_categories.name"))
