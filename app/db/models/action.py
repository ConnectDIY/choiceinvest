from app.db.base import BaseModel
from sqlalchemy import Column, String


class Action(BaseModel):
    __tablename__ = "actions"

    name = Column(String(16))
