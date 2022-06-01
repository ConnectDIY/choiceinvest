from app.db.base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Wallet(BaseModel):
    __tablename__ = "wallets"

    owner = relationship("User", back_populates="wallets")
    description = Column(String)
