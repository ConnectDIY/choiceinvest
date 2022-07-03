from app.db.base import Base, BaseModel
from sqlalchemy import Column, String, Float


class AmortizationInfo(BaseModel):
    __tablename__ = "amortization_info"

    security = Column(String(32))
    action = Column(String(32))
    price = Column(Float)
    value = Column(Float)
