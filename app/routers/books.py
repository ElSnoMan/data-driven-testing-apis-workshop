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


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}
