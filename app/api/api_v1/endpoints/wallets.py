from fastapi import APIRouter

from app.schemas.wallet import WalletInDB

router = APIRouter()

wallets = []

ROOT_ROUTE = '/users/{user_id}/wallets'


@router.post(ROOT_ROUTE)
def create_wallet(wallet: WalletInDB):
    wallets.append(WalletInDB)


@router.get(ROOT_ROUTE)
def get_user_wallets(user_id: int):
    """Returns the user wallets."""
    return wallets


@router.get(ROOT_ROUTE + "/{wallet_id}")
def get_user_wallet(user_id: int, wallet_id: int):
    """Returns the user wallets."""
    for w in wallets:
        if w.owner_id == user_id:
            return w
