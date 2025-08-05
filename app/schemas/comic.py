from pydantic import BaseModel

class ComicOut(BaseModel):
    id: int
    title: str
    author: str
    description: str
    genre: str
    status: str
    rating: float
    chapters: int
    isTrending: bool
    imageUrl: str