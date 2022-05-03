from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Wallet(BaseModel):
    __tablename__ = "wallets"

    owner = relationship("User", back_populates="wallets")
    description = Column(String)
