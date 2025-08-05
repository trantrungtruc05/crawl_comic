from fastapi import FastAPI
from app.api import chapter, chapter_content
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chapter.router, prefix="/api", tags=["Chapters"])

app.include_router(chapter_content.router, prefix="/api", tags=["Chapters Content"])