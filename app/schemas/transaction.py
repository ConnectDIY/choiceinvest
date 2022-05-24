from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.action import Action
from app.schemas.security_type import SecurityType


class Transaction(BaseModel):
    id: int
    action: Action
    price: float
    value: float
    timestamp: int
    fee: float
