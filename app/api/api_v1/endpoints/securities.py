from fastapi import APIRouter

from app.schemas.security import Security

router = APIRouter()

@router.post("/users/{user_id}/wallets/{wallet_id}/securities")
async def create_security(security: Security):
    # Add security to DB
    pass


@router.get("/users/{user_id}/wallets/{wallet_id}/securities")
async def get_securities(user_id: int, wallet_id: int):
    # Retrieve securities from DB
    pass

@router.get("/users/{user_id}/wallets/{wallet_id}/securities")
async def get_security(user_id: int, wallet_id: int, security: Security):
    # Retrieve security from DB
    pass

