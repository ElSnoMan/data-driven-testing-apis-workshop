import pytest

from bookstore.actions.alerts import AlertActions
from bookstore.actions.profile import ProfileActions


@pytest.fixture
def alert(py):
    return AlertActions(py)


@pytest.fixture
def profile(py):
    return ProfileActions(py)
