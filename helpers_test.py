import pytest
import requests_mock
import json

from helpers import google_book_search, parse_search, parse_authors, parse_thumbnail

with open("mock.json") as f:
    mock_json = f.read()

parse_data = {"status": 200, "body": json.loads(mock_json)}


@pytest.fixture
def mock():
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, text=mock_json)


class TestGoogleBookSearch(object):
    def test_search_returns_200(self, mock):
        """Ensure a basic search returns a 200 request"""
        assert google_book_search("Harry Potter")["status"] == 200

    def test_search_body_returns_dict(self, mock):
        """Ensure we're getting a JSON dict back from google_book_search()"""
        assert type(google_book_search("Harry Potter")["body"]) is dict


class TestParseAuthors(object):
    def test_parse_authors_returns_csv_string(self):
        assert parse_authors(["William Shakespeare", "Bill Bryson", "George Saunders"]
                             ) == "William Shakespeare, Bill Bryson, George Saunders"

    def test_parse_empty_authors(self):
        assert parse_authors("") == ""


class TestParseThumbnail(object):
    def test_parse_thumbnail_adds_generic_thumbnail(self):
        assert parse_thumbnail(
            "") == {"thumbnail": "static/generic-book-cover.jpg"}

    def test_parse_thumbnail_returns_valid_unchanged_dict(self):
        thumb_dict = {"smallThumbnail": "www.internet.com/covers/tomThumb.png",
                      "thumbnail": "www.internet.com/covers/cover.png"}
        assert parse_thumbnail(thumb_dict) == thumb_dict


class TestParseSearch(object):
    def test_parse_returns_twenty_objects(self):
        """Ensure parse_search() returns a JSON response with a list of 20 values as the value to the items key"""
        assert len(parse_search(parse_data)["items"]) == 20

    def test_parse_items_are_dicts(self):
        assert type(parse_search(parse_data)["items"][0]) is dict

    def test_parse_returns_author(self):
        """Ensure the parse returns an author key with correct value"""
        book = parse_search(parse_data)["items"][0]
        assert book["authors"] == "J.K. Rowling"

    def test_parse_returns_title(self):
        """Ensure the parse returns a book title with correct value"""
        book = parse_search(parse_data)["items"][1]
        assert book[
            "title"] == "Harry Potter and the Cursed Child – Parts One and Two (Special Rehearsal Edition)"

    def test_parse_returns_publisher(self):
        """Ensure the parse returns a publisher key with correct value"""
        book = parse_search(parse_data)["items"][2]
        assert book["publisher"] == "Bloomsbury Publishing"

    def test_parse_returns_thumbnail(self):
        """Ensure the parse returns an thumbnail key with correct value"""
        book = parse_search(parse_data)["items"][3]
        assert book["imageLinks"]["thumbnail"] == "http://books.google.com/books/content?id=MnSHDAAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
