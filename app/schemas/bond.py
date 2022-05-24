from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.security_type import SecurityType


class Bond(BaseModel):
    id: int
    instrument: int
    value: float
