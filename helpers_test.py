import pytest
from helpers import google_book_search


def test_search_returns_200():
    assert google_book_search("Eloquent Javascript")["status"] == 200


def test_search_body_returns_dict():
    assert type(google_book_search("Eloquent Javascript")["body"]) is dict
