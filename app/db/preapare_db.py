from app.db.models import *
from app.db.base import Base
from app.db import engine


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    pass


if __name__ == '__main__':
    create_tables()
