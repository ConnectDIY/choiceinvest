import os

from sqlalchemy.orm import Session

from app.db.models import *
from app.db.base import Base
from app.db import engine
from dotenv import load_dotenv

from app.db.session import get_db, SessionLocal

load_dotenv()


def create_tables():
    Base.metadata.create_all(engine, checkfirst=False)


def drop_tables():
    Base.metadata.drop_all(engine)


def push_startup_refdata():
    session: Session = SessionLocal()

    # Create superuser
    u = User(
        name=os.environ["APP_ROOT_USER_NAME"],
        password=os.environ["APP_ROOT_USER_PASSWORD"],
        is_active=True,
        is_superuser=True
    )

    session.add(u)

    # Create transaction actions

    session.commit()



if __name__ == '__main__':
    create_tables()
