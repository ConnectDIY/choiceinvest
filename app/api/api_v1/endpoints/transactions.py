from typing import Optional

from fastapi import APIRouter

from app.schemas.security import Security

router = APIRouter()


@router.get("/transactions")
async def get_transactions(user_id: Optional[int], wallet_id: Optional[int]):
    # Retrieve transactions from DB
    pass


@router.get("/transactions")
async def get_transaction(user_id: Optional[int], wallet_id: Optional[int]):
    # Retrieve transactions from DB
    pass
