from app.db.base import Base
from sqlalchemy import Column, String


class InterestType(Base):
    __tablename__ = "interest_types"

    name = Column(String(32), primary_key=True)
