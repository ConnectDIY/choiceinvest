from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

users = []


class User(BaseModel):
    name: str
    password: str
    email: EmailStr


@router.post("/users")
async def create_user(name: str, password: str, email: EmailStr):
    print(name, password, email)
    users.append(User(name=name, password=password, email=email))


@router.get("/users")
async def get_users():
    return users
