import pytest
from billy.utils.search import google_book_search


class TestGoogleBookSearch(object):
    def test_search_returns_200(self, mock):
        """Ensure a basic search returns a 200 request"""
        assert google_book_search("Harry Potter")["status"] == 200

    def test_search_body_returns_dict(self, mock):
        """Ensure we're getting a JSON dict back from google_book_search()"""
        assert type(google_book_search("Harry Potter")["body"]) is dict
