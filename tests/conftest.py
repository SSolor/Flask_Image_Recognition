'''setup for tests basically'''
import pytest
from app import app

@pytest.fixture
def client():
    '''allows it to use app'''
    with app.test_client() as client:
        yield client
