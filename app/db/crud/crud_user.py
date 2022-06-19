from typing import Any

from sqlalchemy.orm import Session

from app import schemas
from app.db import models
from app.db.crud.base import CRUDBase
from app.db.models import User
from app.schemas import UserCreate, UserUpdate

import logging

logger = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            name=obj_in.name,
            password=obj_in.password,
            is_active=True,
            is_superuser=False,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def deactivate(self, db:Session, id: Any):
        pass


user = CRUDUser(User)
