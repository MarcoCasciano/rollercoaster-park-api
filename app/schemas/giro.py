from datetime import datetime

from pydantic import BaseModel


class GiroBase(BaseModel):
    visitatore_id: int
    attrazione_id: int
    ciclo: int = 0


class GiroCreate(GiroBase):
    pass


class GiroRead(GiroBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
