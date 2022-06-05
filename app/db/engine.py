import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get("SQLALCHEMY_DATABASE_URI"), pool_pre_ping=True)
