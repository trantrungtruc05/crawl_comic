from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chapter import ChapterCreate, ChapterOut
from app.crud import chapter
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/chapters/{comic_id}", response_model=list[ChapterOut])
def read_all(comic_id: int, db: Session = Depends(get_db)):
    return chapter.get_chapters(db, comic_id)