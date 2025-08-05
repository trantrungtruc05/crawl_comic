from sqlalchemy import Boolean, Column, Float, Integer, String
from app.db.base import Base


class Comic(Base):
    __tablename__ = "comic"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    description = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    status = Column(String, nullable=True)
    rating = Column(Float, nullable=True)
    chapters = Column(Integer, nullable=True)
    isTrending = Column(Boolean, nullable=True)
    imageUrl = Column(String, nullable=True)
    
