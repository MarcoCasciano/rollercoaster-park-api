from sqlalchemy.orm import Session

from app.db.models.visitatore import Visitatore
from app.schemas.visitatore import VisitatoreCreate, VisitatoreUpdate


def get(db: Session, visitatore_id: int) -> Visitatore | None:
    return db.query(Visitatore).filter(Visitatore.id == visitatore_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Visitatore]:
    return db.query(Visitatore).offset(skip).limit(limit).all()


def create(db: Session, data: VisitatoreCreate) -> Visitatore:
    obj = Visitatore(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, obj: Visitatore, data: VisitatoreUpdate) -> Visitatore:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, obj: Visitatore) -> None:
    db.delete(obj)
    db.commit()
