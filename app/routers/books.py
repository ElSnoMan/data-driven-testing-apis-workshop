from typing import List, Union

from fastapi import APIRouter

from app.mocks import FASTAPI_MOCKED_BOOKS
from app.models.books import BookModel

router = APIRouter()


def validate_book_model_schema(books) -> Union[List[BookModel], BookModel]:
    if isinstance(books, List):
        return [BookModel(**book) for book in books]
    return BookModel(**books)


@router.get('/books/', tags=['books'], response_model=List[BookModel])
async def get_all_books():
    books = validate_book_model_schema(FASTAPI_MOCKED_BOOKS)
    return books


@router.get('/books/search/{query}', tags=['books'], response_model=List[BookModel])
async def search_books(query: str):
    books = validate_book_model_schema(FASTAPI_MOCKED_BOOKS)
    matched_books = []
    query = query.lower()
    for book in books:
        if query in book.title.lower() or query in book.author.lower() or query in book.publisher.lower():
            matched_books.append(book)
    return matched_books
