from hashlib import md5
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.db import crud
from app.db.session import get_db

from app.schemas.user import User, UserCreate

router = APIRouter()


@router.post("/users", response_model=User)
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    return crud.user.create(db=db, obj_in=user_create)


@router.get("/users", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.user.get_multi(db, skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id, db: Session = Depends(get_db)):
    """Returns the concrete user from DB."""
    return crud.user.get(db, user_id)
