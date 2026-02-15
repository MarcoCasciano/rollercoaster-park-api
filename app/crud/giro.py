from sqlalchemy.orm import Session

from app.db.models.giro import Giro
from app.schemas.giro import GiroCreate


def get(db: Session, giro_id: int) -> Giro | None:
    return db.query(Giro).filter(Giro.id == giro_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Giro]:
    return db.query(Giro).offset(skip).limit(limit).all()


def create(db: Session, data: GiroCreate) -> Giro:
    obj = Giro(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, obj: Giro) -> None:
    db.delete(obj)
    db.commit()
