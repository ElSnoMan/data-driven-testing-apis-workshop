from typing import Tuple, Dict

import requests
from requests import Response

from bookstore.models import User, Token

ACCOUNT_V1_URL = "https://demoqa.com/Account/v1"


def create_authorized_user(username, password) -> Tuple[User, Token]:
    user = create_user(username, password)
    token = generate_token(username, password)
    return user, token


def create_user(username, password) -> User:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_V1_URL}/User', json=payload)
    if not response.ok:
        raise ConnectionError(f'Unable to create user: {response.content}')
    return User(**response.json())


def generate_token(username, password) -> Token:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_V1_URL}/GenerateToken', json=payload)
    if not response.ok:
        raise ConnectionError(f'Unable to generate token: {response.content}')
    return Token(**response.json())


def is_authorized(username, password) -> bool:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_V1_URL}/Authorized', json=payload)
    if not response.ok:
        raise ConnectionError(f'Unable to authorize user: {response.content}')
    return response.json()


def delete_user(user_id, token) -> Response:
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{ACCOUNT_V1_URL}/User/{user_id}', headers=headers)
    if not response.ok:
        raise ConnectionError(f'Unable to delete user: {response.content}')
    return response


def get_user(user_id, token) -> Dict:
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{ACCOUNT_V1_URL}/User/{user_id}', headers=headers)
    if not response.ok:
        raise ConnectionError(f'Unable to get user: {response.content}')
    return response.json()
