from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chapter_content import ChapterContentOut
from app.crud import chapter_content
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/content/{chapter_id}", response_model=list[ChapterContentOut])
def read_all(chapter_id: int, db: Session = Depends(get_db)):
    return chapter_content.get_chapters_content(db, chapter_id)