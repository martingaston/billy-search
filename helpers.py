import requests


def google_book_search(search, startIndex=0, maxResults=20):
    """Search the Google Books API for a specified search string and a dict with status code and JSON response"""
    params = {"q": search, 'startIndex': startIndex, 'maxResults': maxResults}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=params)
    return {"status": r.status_code, "body": r.json()}


def parse_search(json):
    # return an empty payload if the response is not 200
    if json["status"] != 200:
        return {"total": 0, "items": []}
    body = json["body"]
    book_list = []
    try:
        for i in body["items"]:
            book = {}

            # check the API responses for existing data - add a empty string if no data is returned from API
            for field in ["authors", "title", "publisher", "imageLinks"]:
                try:
                    book[field] = i["volumeInfo"][field]
                except KeyError:
                    book[field] = ""

            # if API doesn't return a thumbnail, add a generic cover for the search listings
            if not book["imageLinks"]:
                book["imageLinks"] = {
                    "thumbnail": "static/generic-book-cover.jpg"}
            book_list.append(book)
    except KeyError:
        return {"total": 0, "items": []}

    # return our parsed & formatted data
    return {"index": 0, "total": body["totalItems"], "items": book_list}
