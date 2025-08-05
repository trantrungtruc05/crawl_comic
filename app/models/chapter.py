from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

ChapterBase = declarative_base()

class Chapter(ChapterBase):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    link = Column(String, nullable=True)
    comic_id = Column(Integer, nullable=False)