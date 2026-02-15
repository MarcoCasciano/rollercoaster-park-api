from sqlalchemy.orm import Session

from app.db.models.attrazione import Attrazione
from app.schemas.attrazione import AttrazioneCreate, AttrazioneUpdate


def get(db: Session, attrazione_id: int) -> Attrazione | None:
    return db.query(Attrazione).filter(Attrazione.id == attrazione_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Attrazione]:
    return db.query(Attrazione).offset(skip).limit(limit).all()


def create(db: Session, data: AttrazioneCreate) -> Attrazione:
    obj = Attrazione(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, obj: Attrazione, data: AttrazioneUpdate) -> Attrazione:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, obj: Attrazione) -> None:
    db.delete(obj)
    db.commit()
