import logging

from sqlalchemy.orm import Session

from app.db.crud.base import CRUDBase
from app.db.models import Wallet
from app.schemas import WalletCreate, WalletUpdate

logger = logging.getLogger(__name__)


class CRUDWallet(CRUDBase[Wallet, WalletCreate, WalletUpdate]):

    def create(self, db: Session, *, obj_in: WalletCreate) -> Wallet:
        db_obj = Wallet(
            owner=obj_in.owner_id,
            name=obj_in.name,
            description=obj_in.description
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


wallet = CRUDWallet(Wallet)