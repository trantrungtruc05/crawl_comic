from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chapter_content import ChapterContentOut, ChapterContentCreate
from app.crud import chapter_content, chapter
from app.db.session import SessionLocal
import requests
from bs4 import BeautifulSoup

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/content/{chapter_id}", response_model=list[ChapterContentOut])
def read_all(chapter_id: int, db: Session = Depends(get_db)):
    return chapter_content.get_chapters_content(db, chapter_id)


# @router.post("/chaptersContent/crawl/")
# def create(db: Session = Depends(get_db)):
#     all_chapters = chapter.get_chapters(db, 1)
#     for chap in all_chapters:
#         url = chap.link
#         res = requests.get(url)
#         res.raise_for_status()
#         soup = BeautifulSoup(res.text, "html.parser")
#         img_tags = soup.select("div.container > div.row div#primary img[alt*=\"Truyện Tranh Thám Tử Lừng Danh Conan\"]")
#         print(len(img_tags))
#         jpg_links = []
#         for img in img_tags:
#             src = img.get("src")
#             print("https://dilib.vn" + src)
#             print(len(img_tags))
#             chapter_content_create = ChapterContentCreate(chapter_id=chap.id, content="https://dilib.vn" + src)
#             chapter_content.create_chapter_content(db, chapter_content_create)

#         print("Crawl " + chap.title + " done")

#     return {"message": "Crawled chapter content successfully"}