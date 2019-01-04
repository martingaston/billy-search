import pytest
import flask
from application import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_home_route(client):
    with app.test_client() as c:
        response = c.get("/")
        assert response.status_code == 200


def test_search_route(client):
    with app.test_request_context('/query?search=Harry+Potter'):
        assert flask.request.path == '/query'
        assert flask.request.args['search'] == 'Harry Potter'


def test_empty_search_is_redirected(client):
    with app.test_client() as c:
        response = c.get("/query?search=")
        assert response.status_code == 302


def test_404_route(client):
    with app.test_client() as c:
        response = c.get("/holy-grail")
        assert response.status_code == 404
