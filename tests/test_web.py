import pytest
import json

from web import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    result = client.get("/")
    assert result.status_code == 200
    assert {"hello": "bob"} == json.loads(result.get_data(as_text=True))

def test_change(app, client):
    result = client.get("/change/1/34")
    assert result.status_code == 200
    assert [{'5': 'quarters'}, {'1': 'nickels'}, {'4': 'pennies'}] == json.loads(result.get_data(as_text=True))