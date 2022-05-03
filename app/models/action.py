from app.models.base import BaseModel
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship


class Action(BaseModel):
    __tablename__ = "actions"

    name = Column(String(16))
