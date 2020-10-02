import pytest
import requests

from bookstore.services import book_service


def test_get_all_books():
    books = book_service.get_all_books()
    assert len(books) == 8  # There are 8 books seeded in the DB


def test_get_single_book():
    isbn = '9781449325862'
    book = book_service.get_book_by_isbn(isbn)
    assert isbn == book.isbn


def test_add_books_to_user():
    pytest.xfail()


def test_delete_all_books_from_user():
    pytest.xfail()


def test_delete_single_book_from_user():
    pytest.xfail()


def test_replace_book_in_collection_by_isbn():
    pytest.xfail()
