from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import comic
from app.db.session import SessionLocal
from app.schemas.comic import ComicOut




router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/comics", response_model=list[ComicOut])
def read_all(db: Session = Depends(get_db)):
    return comic.get_comics(db)