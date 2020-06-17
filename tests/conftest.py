import pytest
from medc import create_app

@pytest.fixture
def app():
    return create_app()

