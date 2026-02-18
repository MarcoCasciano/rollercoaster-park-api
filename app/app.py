from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api_router
from app.db.database import engine
from app.db.base import Base

# Importa tutti i modelli per registrarli con Base.metadata
from app.db.models import attrazione, famiglia, visitatore, giro  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Rollercoaster Park API", lifespan=lifespan)

app.include_router(api_router)
