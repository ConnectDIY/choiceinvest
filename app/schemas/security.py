from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.security_type import SecurityType


class Security(BaseModel):
    id: int
    type_id: SecurityType
    wallet_id: int
