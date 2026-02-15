from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import attrazione as crud
from app.db.database import get_db
from app.schemas.attrazione import AttrazioneCreate, AttrazioneRead, AttrazioneUpdate

router = APIRouter(prefix="/attrazioni", tags=["attrazioni"])


@router.get("/", response_model=list[AttrazioneRead])
def list_attrazioni(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/{attrazione_id}", response_model=AttrazioneRead)
def get_attrazione(attrazione_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, attrazione_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Attrazione non trovata")
    return obj


@router.post("/", response_model=AttrazioneRead, status_code=201)
def create_attrazione(data: AttrazioneCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


@router.patch("/{attrazione_id}", response_model=AttrazioneRead)
def update_attrazione(attrazione_id: int, data: AttrazioneUpdate, db: Session = Depends(get_db)):
    obj = crud.get(db, attrazione_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Attrazione non trovata")
    return crud.update(db, obj, data)


@router.delete("/{attrazione_id}", status_code=204)
def delete_attrazione(attrazione_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, attrazione_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Attrazione non trovata")
    crud.delete(db, obj)
