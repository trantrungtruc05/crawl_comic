from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

ChapterContentBase = declarative_base()

class ChapterContent(ChapterContentBase):
    __tablename__ = "chapter_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chapter_id = Column(Integer, nullable=False)
    content = Column(String, nullable=True)