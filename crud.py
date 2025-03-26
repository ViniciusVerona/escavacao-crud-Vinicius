from sqlalchemy.orm import Session
from models import ExcavationPoint
from schemas import ExcavationPointCreate
from datetime import datetime
from typing import Optional

def create_point(db: Session, data: ExcavationPointCreate) -> ExcavationPoint:
    point = ExcavationPoint(**data.dict(), discovered_at=datetime.utcnow())
    db.add(point)
    db.commit()
    db.refresh(point)
    return point

def get_all_points(db: Session) -> list[ExcavationPoint]:
    return db.query(ExcavationPoint).all()

def get_point_by_id(db: Session, point_id: int) -> Optional[ExcavationPoint]:
    return db.query(ExcavationPoint).filter(ExcavationPoint.id == point_id).first()

def update_point(db: Session, point_id: int, data: dict) -> Optional[ExcavationPoint]:
    point = get_point_by_id(db, point_id)
    if point:
        for key, value in data.items():
            setattr(point, key, value)
        db.commit()
        db.refresh(point)
    return point

def delete_point(db: Session, point_id: int) -> bool:
    point = get_point_by_id(db, point_id)
    if point:
        db.delete(point)
        db.commit()
        return True
    return False
