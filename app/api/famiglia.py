from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import famiglia as crud
from app.db.database import get_db
from app.schemas.famiglia import FamigliaCreate, FamigliaRead, FamigliaUpdate

router = APIRouter(prefix="/famiglie", tags=["famiglie"])


@router.get("/", response_model=list[FamigliaRead])
def list_famiglie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/{famiglia_id}", response_model=FamigliaRead)
def get_famiglia(famiglia_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, famiglia_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Famiglia non trovata")
    return obj


@router.post("/", response_model=FamigliaRead, status_code=201)
def create_famiglia(data: FamigliaCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


@router.patch("/{famiglia_id}", response_model=FamigliaRead)
def update_famiglia(famiglia_id: int, data: FamigliaUpdate, db: Session = Depends(get_db)):
    obj = crud.get(db, famiglia_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Famiglia non trovata")
    return crud.update(db, obj, data)


@router.delete("/{famiglia_id}", status_code=204)
def delete_famiglia(famiglia_id: int, db: Session = Depends(get_db)):
    obj = crud.get(db, famiglia_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Famiglia non trovata")
    crud.delete(db, obj)
