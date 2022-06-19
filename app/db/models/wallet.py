from app.db.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Wallet(BaseModel):
    __tablename__ = "wallets"

    owner = Column(Integer, ForeignKey("users.id"))
    name = Column(String(32))
    description = Column(String)
