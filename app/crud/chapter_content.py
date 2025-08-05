from sqlalchemy.orm import Session
from app.models.chapter_content import ChapterContent



def get_chapters_content(db: Session, chapter_id: int):
    return db.query(ChapterContent).filter(ChapterContent.chapter_id == chapter_id).all()