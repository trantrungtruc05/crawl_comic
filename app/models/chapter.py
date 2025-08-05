from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    link = Column(String, nullable=True)
    comic_id = Column(Integer, nullable=False)