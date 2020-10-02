import pytest
import requests

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


def test_create_user(credentials, new_unauthorized_user):
    user = new_unauthorized_user
    assert user.username == credentials.get('username')


def test_generate_token(new_authorized_user):
    _, token = new_authorized_user
    assert len(token.token) > 0  # not an empty string


def test_create_authorized_user(credentials, new_authorized_user):
    assert account_service.is_authorized(**credentials)


def test_create_unauthorized_user(credentials, new_unauthorized_user):
    assert account_service.is_authorized(**credentials) is False


def test_cannot_delete_unauthorized_user(credentials):
    user = account_service.create_user(**credentials)
    with pytest.raises(ConnectionError):
        account_service.delete_user(user.userID, None)


def test_delete_authorized_user(credentials):
    user, token = account_service.create_authorized_user(**credentials)
    response = account_service.delete_user(user.userID, token.token)
    assert response.ok


def test_get_user(new_authorized_user):
    new_user, token = new_authorized_user
    user = account_service.get_user(new_user.userID, token.token)
    assert new_user.userID == user.get('userId')
