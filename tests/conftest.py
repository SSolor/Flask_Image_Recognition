'''setup for tests basically'''
import pytest
from app import app

@pytest.fixture
def client():
    '''allows it to use app'''
    app.config["TESTING"] = True
    with app.test_client() as tclient:
        yield tclient
