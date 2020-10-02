from typing import List

from pydantic import BaseModel, Field


class Book(BaseModel):
    isbn: str
    title: str
    sub_title: str = Field(alias='subTitle')
    author: str
    publish_date: str
    publisher: str
    pages: int
    description: str
    website: str


class User(BaseModel):
    userID: str
    username: str
    books: List[Book]


class Token(BaseModel):
    token: str
    expires: str
    status: str
    result: str
