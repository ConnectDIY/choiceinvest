from app.db.base import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(64))
    password = Column(String(64))
    # email = Column()
    # role = Column()
