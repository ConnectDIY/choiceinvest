from hashlib import md5

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.schemas.user import User, UserCreate, UserInDB

router = APIRouter()

users = []

last_id = 0


def gen_id() -> int:
    global last_id
    last_id += 1
    return last_id


@router.post("/users")
async def create_user(user_create: UserCreate):
    users.append(UserInDB(name=user_create.name,
                          email=user_create.email,
                          id=gen_id(),
                          hashed_password=md5(user_create.password.encode()).hexdigest()
                          ))


@router.get("/users")
async def get_users():
    return users


@router.get("/users/{user_id}")
async def get_user(user_id):
    """Returns the concrete user from DB."""
    return users
