from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.category_type import CategoryType
from app.schemas.interest_type import InterestType


class BondInstrument(BaseModel):
    isin: int
    name: str
    interest: float
    interest_type: InterestType
    maturity_data: date
    face_value: float
    yield_to_maturity: float
    category: CategoryType
