import pytest
import requests_mock

from helpers import google_book_search


@pytest.fixture
def mock():
    with open("mock.json") as f:
        mock_json = f.read()
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, text=mock_json)


class Test(object):
    def test_search_returns_200(self, mock):
        """Ensure a basic search returns a 200 request"""
        assert google_book_search("Eloquent Javascript")["status"] == 200

    def test_search_body_returns_dict(self, mock):
        """Ensure we're getting a JSON dict back from google_book_search()"""
        assert type(google_book_search("Eloquent Javascript")["body"]) is dict
