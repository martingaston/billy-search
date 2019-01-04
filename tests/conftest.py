import pytest
import requests_mock
import json
from billy import create_app
from billy.utils import BookList


@pytest.fixture
def app():

    app = create_app({
        'TESTING': True
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


# read our mock JSON data to mock_json
with open("tests/mock.json") as f:
    mock_json = f.read()


@pytest.fixture
def mock():
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, text=mock_json)


@pytest.fixture
def book_list():
    mock = {"status": 200, "body": json.loads(mock_json)}
    return BookList(testing=mock)
