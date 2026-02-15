from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import visitatore as crud
from app.db.database import get_db
from app.schemas.visitatore import VisitatoreCreate, VisitatoreRead, VisitatoreUpdate

router = APIRouter(prefix="/visitatori", tags=["visitatori"])


@router.get("/", response_model=list[VisitatoreRead])
def list_visitatori(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/{visitatore_id}", response_model=VisitatoreRead)
def get_visitatore(visitatore_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, visitatore_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Visitatore non trovato")
    return obj


@router.post("/", response_model=VisitatoreRead, status_code=201)
def create_visitatore(data: VisitatoreCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


@router.patch("/{visitatore_id}", response_model=VisitatoreRead)
def update_visitatore(visitatore_id: int, data: VisitatoreUpdate, db: Session = Depends(get_db)):
    obj = crud.get(db, visitatore_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Visitatore non trovato")
    return crud.update(db, obj, data)


@router.delete("/{visitatore_id}", status_code=204)
def delete_visitatore(visitatore_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, visitatore_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Visitatore non trovato")
    crud.delete(db, obj)
