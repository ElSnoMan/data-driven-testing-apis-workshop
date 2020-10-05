import pytest

from bookstore import mocks
from bookstore.models import Book
from bookstore.services import account_service, book_service


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


@pytest.fixture
def user_with_books(new_authorized_user, mocked_books):
    user, token = new_authorized_user
    book_service.add_books_to_user(user.userID, token.token, mocked_books)
    return user, token


@pytest.fixture
def login_seam(py, new_authorized_user):
    def _login(next_url_path):
        base_url = 'https://demoqa.com'
        user, token = new_authorized_user
        py.visit(f'{base_url}/login')
        py.set_cookie({'name': 'userName', 'value': user.username})
        py.set_cookie({'name': 'userID', 'value': user.userID})
        py.set_cookie({'name': 'token', 'value': token.token})
        py.set_cookie({'name': 'expires', 'value': token.expires})
        py.visit(f'{base_url}{next_url_path}')
        return user, token
    return _login
