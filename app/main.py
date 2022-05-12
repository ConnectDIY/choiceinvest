from fastapi import FastAPI
from app.api.api_v1.endpoints import users

app = FastAPI(version='0.0.1')

app.include_router(users.router)