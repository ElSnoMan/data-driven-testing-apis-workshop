import pytest
import requests
from pydantic import ValidationError

from app import mocks
from app.routers.books import validate_book_model_schema

BASE_URL = 'http://localhost:8000'


def test_validate_book_model_schema():
    books = validate_book_model_schema(mocks.FASTAPI_MOCKED_BOOKS)
    assert len(books) == 8


invalid_error_messages = ['value_error.missing',
                          'value_error.missing',
                          'ensure this value has at least 10 characters',
                          'none is not an allowed value',
                          'value_error.missing']
invalid_schema_examples = zip(mocks.FASTAPI_MOCKED_INVALID_BOOKS, invalid_error_messages)


@pytest.mark.parametrize('book, error_message', invalid_schema_examples)
def test_validate_book_model_schema_raises_error_with_invalid_body(book, error_message):
    with pytest.raises(ValidationError) as error:
        validate_book_model_schema(book)

    error = str(error.value)
    assert error_message in error


def test_get_all_books():
    response = requests.get(f'{BASE_URL}/books/')
    assert response.ok


exact_search_examples = [
    ("Git Pocket Guide", 1),
    ("eric elliot", 1),
    ("O'Reilly Media", 6),
    ("Carlos Kidman", 0)
]


@pytest.mark.parametrize('query, result', exact_search_examples)
def test_user_enters_an_exact_search(query, result):
    response = requests.get(f'{BASE_URL}/books/search/{query}')
    assert response.ok

    books = response.json()
    assert len(books) == result


fuzzy_search_examples = [
    ("javascript", 4),
    ("a", 8),
    ("as", 6),
    ("asf", 0)
]


@pytest.mark.parametrize('query, result', fuzzy_search_examples)
def test_user_enters_a_fuzzy_search(query, result):
    response = requests.get(f'{BASE_URL}/books/search/{query}')
    assert response.ok

    books = response.json()
    assert len(books) == result
