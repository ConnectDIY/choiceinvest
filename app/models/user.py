from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(64))
    password = Column(String(64))
    # email = Column()
    # role = Column()
