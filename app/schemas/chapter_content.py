from pydantic import BaseModel

class ChapterContentOut(BaseModel):
    id: int
    content: str

class ChapterContentCreate(BaseModel):
    chapter_id: int
    content: str