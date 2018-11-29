import pytest
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


def test_404_route(client):
    with app.test_client() as c:
        response = c.get("/holy-grail")
        assert response.status_code == 404
