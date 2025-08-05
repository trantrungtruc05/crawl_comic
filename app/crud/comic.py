from sqlalchemy.orm import Session
from app.models.comic import Comic


def get_comics(db: Session):
    return db.query(Comic).all()