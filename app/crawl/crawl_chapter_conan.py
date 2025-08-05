import requests
from bs4 import BeautifulSoup
from db.session import SessionLocal, init_db
from models.chapter import Chapter

init_db()

url = "https://dilib.vn/tham-tu-lung-danh-conan-14786.html"

# Gửi request lấy HTML
res = requests.get(url)
res.raise_for_status()

# Parse HTML
soup = BeautifulSoup(res.text, "html.parser")

a_tags = soup.select("div.container > div.row div#primary fieldset > div.row > div > a")
print(len(a_tags))

session = SessionLocal()

for a in a_tags:
    chapter = Chapter(title=a.get_text(strip=True), link="https://dilib.vn" + a.get("href"), comic_id=1)
    session.add(chapter)

session.commit()
session.close()
print("Done")