import pytest
from flask import request


def test_home_route(client):
    with client as c:
        response = c.get("/")
        assert response.status_code == 200


def test_home_route_renders(client):
    with client as c:
        response = c.get("/")
        assert b'<title>Billy Booksearch</title>' in response.data
        assert b'alt="bookcase"' in response.data
        assert b'id="search"' in response.data
        assert b'id="search_button"' in response.data


def test_search_route(client):
    with client as c:
        _response = c.get("/query?search=Harry+Potter")
        assert request.path == '/query'
        assert request.args['search'] == 'Harry Potter'


def test_search_route_renders(client):
    with client as c:
        response = c.get("/query?search=Harry+Potter")
        assert b'id="search"' in response.data
        assert b'id="next"' in response.data


def test_empty_search_is_redirected(client):
    with client as c:
        response = c.get("/query?search=")
        assert response.status_code == 302


def test_404_route(client):
    with client as c:
        response = c.get("/holy-grail")
        assert response.status_code == 404
