from sqlalchemy import Column, Integer, String
from app.db.base import Base



class ChapterContent(Base):
    __tablename__ = "chapter_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chapter_id = Column(Integer, nullable=False)
    content = Column(String, nullable=True)