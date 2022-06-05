from fastapi import FastAPI
from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import wallets
from app.db import SessionLocal

from app.db.preapare_db import create_tables

try:
    create_tables()
except Exception as e:
    print(e)
    pass

app = FastAPI(version='0.0.1')

app.include_router(users.router)
app.include_router(wallets.router)
