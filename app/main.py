from fastapi import FastAPI
from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import wallets
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s | %(asctime)s | %(name)s | %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

from app.db.preapare_db import create_tables

try:
    logger.info("Try create tables")
    create_tables()
except Exception as e:
    logger.exception(e)


logger.info('Run FastAPI server')
app = FastAPI(version='0.0.1')

app.include_router(users.router)
app.include_router(wallets.router)
