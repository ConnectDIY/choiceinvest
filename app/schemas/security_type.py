from typing import Optional

from pydantic import BaseModel, EmailStr


class SecurityType(BaseModel):
    name: str
