from sqlalchemy.orm import Session
from app.models.chapter_content import ChapterContent
from app.schemas.chapter_content import ChapterContentCreate




def get_chapters_content(db: Session, chapter_id: int):
    return db.query(ChapterContent).filter(ChapterContent.chapter_id == chapter_id).all()

def create_chapter_content(db: Session, chapter_content: ChapterContentCreate):
    db_link = ChapterContent(**chapter_content.model_dump())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link