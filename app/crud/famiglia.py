from sqlalchemy.orm import Session

from app.db.models.famiglia import Famiglia
from app.schemas.famiglia import FamigliaCreate, FamigliaUpdate


def get(db: Session, famiglia_id: int) -> Famiglia | None:
    return db.query(Famiglia).filter(Famiglia.id == famiglia_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Famiglia]:
    return db.query(Famiglia).offset(skip).limit(limit).all()


def create(db: Session, data: FamigliaCreate) -> Famiglia:
    obj = Famiglia(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, obj: Famiglia, data: FamigliaUpdate) -> Famiglia:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, obj: Famiglia) -> None:
    db.delete(obj)
    db.commit()
