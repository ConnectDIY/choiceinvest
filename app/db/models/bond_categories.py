from app.db.base import Base
from sqlalchemy import Column, String


class BondCategory(Base):
    __tablename__ = "bond_categories"

    name = Column(String(32), primary_key=True)
