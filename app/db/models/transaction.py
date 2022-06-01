from app.db.base import BaseModel


class Transaction(BaseModel):
    __tablename__ = "transactions"

    security = None
    action = None
    price = None
    value = None
