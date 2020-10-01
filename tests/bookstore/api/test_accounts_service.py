import pytest
import requests


ACCOUNT_V1_URL = "https://demoqa.com/Account/v1"


def test_create_authorized_user():
    payload = {'userName': 'CarlosKidman', 'password': 'P@$$w0rd'}
    user_response = requests.post(f'{ACCOUNT_V1_URL}/User', json=payload)
    token_response = requests.post(f'{ACCOUNT_V1_URL}/GenerateToken', json=payload)
    auth_response = requests.post(f'{ACCOUNT_V1_URL}/Authorized', json=payload)
    assert auth_response.ok
    assert auth_response.json() is True


def test_create_unauthorized_user():
    payload = {'userName': 'CarlosKidman', 'password': 'P@$$w0rd'}
    user_response = requests.post(f'{ACCOUNT_V1_URL}/User', json=payload)
    assert user_response.ok
    auth_response = requests.post(f'{ACCOUNT_V1_URL}/Authorized', json=payload)
    assert auth_response.ok
    assert auth_response.json() is False


def test_delete_user():
    pytest.xfail()


def test_get_user():
    pytest.xfail()
