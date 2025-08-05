import requests
from bs4 import BeautifulSoup
from db.session import SessionLocal, init_db
from models.chapter import Chapter
from models.chapter_content import ChapterContent

init_db()

session = SessionLocal()
all_chapters = session.query(Chapter).filter(Chapter.comic_id == 1).all()
for chapter in all_chapters:
    url = chapter.link
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    img_tags = soup.select("div.container > div.row div#primary img[alt*=\"Truyện Tranh Thám Tử Lừng Danh Conan\"]")
    print(len(img_tags))

    jpg_links = []
    for img in img_tags:
        src = img.get("src")
        print("https://dilib.vn" + src)
        print(len(img_tags))
        chapter_content = ChapterContent(chapter_id=chapter.id, content="https://dilib.vn" + src)
        session.add(chapter_content)

    print("Crawl " + chapter.title + " done")



session.commit()
session.close()






