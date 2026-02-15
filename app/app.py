from fastapi import FastAPI

from app.api import api_router
from app.db.database import engine
from app.db.base import Base

# Importa tutti i modelli per registrarli con Base.metadata
from app.db.models import attrazione, famiglia, visitatore, giro  # noqa: F401

app = FastAPI(title="Rollercoaster Park API")

app.include_router(api_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
