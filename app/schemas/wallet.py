from typing import Optional

from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str
    owner_id: int
    description: Optional[str]


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass


class WalletInDBBase(WalletBase):
    id: int

    class Config:
        orm_mode = True


class Wallet(WalletInDBBase):
    pass
