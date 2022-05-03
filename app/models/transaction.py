from app.models.base import BaseModel
from sqlalchemy import Column, Float
from sqlalchemy.orm import relationship


class Transaction(BaseModel):
    __tablename__ = "transactions"

    security = None
    action = None
    price = None
    value = None
