from sqlalchemy.orm import Session
from app.models.chapter import Chapter



def get_chapters(db: Session, comic_id: int):
    return db.query(Chapter).filter(Chapter.comic_id == comic_id).all()