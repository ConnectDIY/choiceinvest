from app.db.base import BaseModel
from sqlalchemy import Column, String, Boolean


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(64))
    password = Column(String(64))
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
    # email = Column()
    # role = Column()
