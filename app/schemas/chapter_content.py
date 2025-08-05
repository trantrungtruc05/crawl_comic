from pydantic import BaseModel

class ChapterContentOut(BaseModel):
    id: int
    content: str