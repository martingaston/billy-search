from .search import google_book_search
from .https import convert_to_https


class BookList():
    def __init__(self, query="", start=0, testing=False, https=False):
        if not testing:
            self.json = google_book_search(query, start)
        else:
            self.json = testing

        self.https = True if https else False

    def parse(self):
        """Take Google Books API JSON as an input and parse into data for application, returning empty payload if error"""

        if self.json["status"] != 200:
            return empty_payload()

        body = self.json["body"]
        book_list = []

        try:
            for i in body["items"]:
                book = {}

                # check the API responses for existing data - add a empty string if no data is returned from API
                for field in ["authors", "title", "publisher", "imageLinks", "infoLink"]:
                    try:
                        book[field] = i["volumeInfo"][field]
                    except KeyError:
                        book[field] = ""

                book["authors"] = self._parse_authors(book["authors"])
                book["imageLinks"] = self._parse_thumbnail(book["imageLinks"])
                book_list.append(book)

        except KeyError:
            return empty_payload()

        return {"total": body["totalItems"], "items": book_list}

    def _parse_authors(self, authors_list=""):
        """Join array of authors into comma-separated string"""
        return ", ".join(authors_list)

    def _parse_thumbnail(self, imageLinks=""):
        """Add generic image to imageLinks if empty, else return input"""
        if not imageLinks:
            return {"thumbnail": "static/generic-book-cover.jpg"}
        else:
            if self.https:
                for link in imageLinks:
                    imageLinks[link] = convert_to_https(imageLinks[link])

            return imageLinks


def payload(items, total):
    return {"total": total, "items": items}


def empty_payload():
    return payload([], 0)
