import pytest
import requests

BASE_URL = 'http://localhost:8000'


def test_get_all_books():
    response = requests.get(f'{BASE_URL}/books/')
    assert response.ok


def test_user_enters_an_exact_search():
    pytest.xfail()


def test_user_enters_a_fuzzy_search():
    pytest.xfail()
