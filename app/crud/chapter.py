from sqlalchemy.orm import Session
from app.models.chapter import Chapter
from app.schemas.chapter import ChapterCreate



def get_chapters(db: Session, comic_id: int):
    return db.query(Chapter).filter(Chapter.comic_id == comic_id).all()

def create_chapter(db: Session, chapter: ChapterCreate):
    db_link = Chapter(**chapter.model_dump())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link