import pytest

from bookstore import mocks
from bookstore.models import Book
from bookstore.services import account_service


@pytest.fixture
def credentials(fake):
    username = fake.first_name() + fake.last_name()
    password = 'P@$$w0rd'
    return {'username': username, 'password': password}


@pytest.fixture
def new_authorized_user(credentials):
    user, token = account_service.create_authorized_user(**credentials)
    yield user, token
    account_service.delete_user(user.userID, token.token)


@pytest.fixture
def new_unauthorized_user(credentials):
    user = account_service.create_user(**credentials)
    yield user
    # need to authorize first, then able to delete
    token = account_service.generate_token(**credentials)
    account_service.delete_user(user.userID, token.token)


@pytest.fixture
def mocked_books():
    return [Book(**book) for book in mocks.MOCKED_BOOKS]
