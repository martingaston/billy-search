import pytest


class TestParseAuthors(object):
    def test_parse_authors_returns_csv_string(self, book_list):
        """Ensure parse_authors() creates a comma separated string if supplied an array of strings"""
        assert book_list._parse_authors(["William Shakespeare", "Bill Bryson", "George Saunders"]
                                        ) == "William Shakespeare, Bill Bryson, George Saunders"

    def test_parse_empty_authors(self, book_list):
        """Ensure parse_authors() returns an empty string if provided with an empty string"""
        assert book_list._parse_authors("") == ""


class TestParseThumbnail(object):
    def test_parse_thumbnail_adds_generic_thumbnail(self, book_list):
        """Ensure parse_thumbnail() returns a dict including generic image thumbnail with no input"""
        assert book_list._parse_thumbnail(
            "") == {"thumbnail": "static/generic-book-cover.jpg"}

    def test_parse_thumbnail_returns_valid_unchanged_dict(self, book_list):
        """Ensure parse_thumbnail() returns the original dict if a dict is supplied as a parameter"""
        thumb_dict = {"smallThumbnail": "www.internet.com/covers/tomThumb.png",
                      "thumbnail": "www.internet.com/covers/cover.png"}
        assert book_list._parse_thumbnail(thumb_dict) == thumb_dict

    def test_parse_thumbnails_converts_to_https(self, book_list):
        """Ensure parse_thumbnail() converts http to https if BookList has https set to True"""
        assert book_list._parse_thumbnail({"smallThumbnail": "http://www.internet.com/covers/tomThumb2.jpg"}) == {
            "smallThumbnail": "https://www.internet.com/covers/tomThumb2.jpg"}


class TestParseSearch(object):
    def test_parse_returns_twenty_objects(self, book_list):
        """Ensure parse_search() returns a JSON response with a list of 20 values as the value to the items key"""
        response = book_list.parse()
        assert len(response["items"]) == 20

    def test_parse_items_are_dicts(self, book_list):
        """Ensure that the parsed data items key is a list of dicts"""
        response = book_list.parse()
        assert type(response["items"][0]) is dict

    def test_parse_returns_author(self, book_list):
        """Ensure the parse returns an author key with correct value"""
        response = book_list.parse()
        book = response["items"][0]
        assert book["authors"] == "J.K. Rowling"

    def test_parse_returns_title(self, book_list):
        """Ensure the parse returns a book title with correct value"""
        response = book_list.parse()
        book = response["items"][1]
        assert book[
            "title"] == "Harry Potter and the Cursed Child – Parts One and Two (Special Rehearsal Edition)"

    def test_parse_returns_publisher(self, book_list):
        """Ensure the parse returns a publisher key with correct value"""
        response = book_list.parse()
        book = response["items"][2]
        assert book["publisher"] == "Bloomsbury Publishing"

    def test_parse_returns_thumbnail(self, book_list):
        """Ensure the parse returns an thumbnail key with correct value"""
        response = book_list.parse()
        book = response["items"][3]
        assert book["imageLinks"]["thumbnail"] == "https://books.google.com/books/content?id=MnSHDAAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"

    def test_parse_returns_info_link(self, book_list):
        """Ensure parsed data returns an infoLink"""
        response = book_list.parse()
        book = response["items"][0]
        assert book["infoLink"] == "http://books.google.co.uk/books?id=wrOQLV6xB-wC&dq=harry+potter&hl=&source=gbs_api"
