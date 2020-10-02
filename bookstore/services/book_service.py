from typing import List

import requests

from bookstore.models import Book

BOOKSTORE_V1_URL = "https://demoqa.com/BookStore/v1"
BOOK_ENDPOINT = f'{BOOKSTORE_V1_URL}/Book'
BOOKS_ENDPOINT = f'{BOOKSTORE_V1_URL}/Books'


def get_all_books() -> List[Book]:
    response = requests.get(BOOKS_ENDPOINT)
    if not response.ok:
        raise ConnectionError(f'Unable to get all books: {response.content}')
    books = response.json()['books']
    return [Book(**book) for book in books]


def get_book_by_isbn(isbn):
    return None