from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.security_type import SecurityType


class Action(BaseModel):
    name: str
