from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import crud
from app.db.session import get_db
from app.schemas.wallet import WalletCreate, Wallet

router = APIRouter()

wallets = []

ROOT_ROUTE = '/users/{user_id}/wallets'


@router.post(ROOT_ROUTE, response_model=Wallet)
def create_wallet(wallet_create: WalletCreate, db: Session = Depends(get_db)):
    return crud.wallet.create(db=db, obj_in=wallet_create)


@router.get(ROOT_ROUTE, response_model=Wallet)
def get_user_wallets(user_id: int, db: Session = Depends(get_db)):
    """Returns the user wallets."""
    return crud.wallet.get_multi(db=db)


@router.get(ROOT_ROUTE + "/{wallet_id}", response_model=Wallet)
def get_user_wallet(user_id: int, wallet_id: int, db: Session = Depends(get_db)):
    """Returns the user wallet."""
    # TODO - add user_id
    return crud.wallet.get(db=db, id=wallet_id)
