from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import giro as crud
from app.db.database import get_db
from app.schemas.giro import GiroCreate, GiroRead

router = APIRouter(prefix="/giri", tags=["giri"])


@router.get("/", response_model=list[GiroRead])
def list_giri(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/{giro_id}", response_model=GiroRead)
def get_giro(giro_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, giro_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Giro non trovato")
    return obj


@router.post("/", response_model=GiroRead, status_code=201)
def create_giro(data: GiroCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


@router.delete("/{giro_id}", status_code=204)
def delete_giro(giro_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, giro_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Giro non trovato")
    crud.delete(db, obj)
