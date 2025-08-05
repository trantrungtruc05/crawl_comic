from pydantic import BaseModel

class ChapterOut(BaseModel):
    id: int
    title: str
    link: str
    comic_id: int

class ChapterCreate(BaseModel):
    title: str
    link: str
    comic_id: int