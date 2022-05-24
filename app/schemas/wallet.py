from typing import Optional

from pydantic import BaseModel


class WalletBase(BaseModel):
    owner_id: int
    description: Optional[str]


class WalletInDBBase(WalletBase):
    id: int

    class Config:
        orm_mode = True


class WalletInDB(WalletInDBBase):
    pass
