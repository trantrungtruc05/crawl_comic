from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chapter import ChapterCreate, ChapterOut
from app.crud import chapter
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


@router.get("/chapters/{comic_id}", response_model=list[ChapterOut])
def read_all(comic_id: int, db: Session = Depends(get_db)):
    return chapter.get_chapters(db, comic_id)

# @router.post("/chapters/crawl/")
# def create(db: Session = Depends(get_db)):
#     url = "https://dilib.vn/tham-tu-lung-danh-conan-14786.html"

#     # Gửi request lấy HTML
#     res = requests.get(url)
#     res.raise_for_status()

#     # Parse HTML
#     soup = BeautifulSoup(res.text, "html.parser")

#     a_tags = soup.select("div.container > div.row div#primary fieldset > div.row > div > a")
#     print(len(a_tags))


#     for a in a_tags:
#         print("zzz " + a.get_text(strip=True))
#         chapterCreate = ChapterCreate(title=a.get_text(strip=True), link="https://dilib.vn" + a.get("href"), comic_id=1)
#         chapter.create_chapter(db, chapterCreate)
#         print("Created chapter: ", a.get_text(strip=True))

#     return {"message": "Crawled chapters successfully"}