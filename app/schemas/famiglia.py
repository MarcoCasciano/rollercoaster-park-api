from pydantic import BaseModel, Field


class FamigliaBase(BaseModel):
    cognome: str = Field(..., min_length=1, max_length=100)
    num_adulti: int = Field(default=1, ge=0)
    num_bambini: int = Field(default=1, ge=0)
    num_ragazzi: int = Field(default=1, ge=0)


class FamigliaCreate(FamigliaBase):
    pass


class FamigliaUpdate(BaseModel):
    cognome: str | None = None
    num_adulti: int | None = Field(default=None, ge=0)
    num_bambini: int | None = Field(default=None, ge=0)
    num_ragazzi: int | None = Field(default=None, ge=0)


class FamigliaRead(FamigliaBase):
    id: int

    class Config:
        from_attributes = True
