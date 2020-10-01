from pydantic import BaseModel, Field


class BookModel(BaseModel):
    author: str
    image: str
    isbn: str = Field(min_length=10, max_length=13)
    publisher: str
    title: str
