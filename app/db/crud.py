from sqlalchemy.orm import Session

from app.db import models
from app import schemas
import logging
logger = logging.getLogger(__name__)

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    logger.info(f'Get users ({skip=}, {limit=})')
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_wallets(db: Session, skip=0, limit=100):
    return db.query(models.Wallet).offset(skip).limit(limit).all()

