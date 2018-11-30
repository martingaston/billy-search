import requests


def google_book_search(search, startIndex=0, maxResults=20):
    params = {"q": search, 'startIndex': startIndex, 'maxResults': maxResults}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=params)
    return {"status": r.status_code, "body": r.json()}


def parse_search(json):
    if json["status"] != 200:
        return {"total": 0, "items": []}
    body = json["body"]
    book_list = []
    try:
        for i in body["items"]:
            book = {}
            for field in ["authors", "title", "publisher", "imageLinks"]:
                try:
                    book[field] = i["volumeInfo"][field]
                except KeyError:
                    book[field] = ""
            book_list.append(book)
    except KeyError:
        return {"total": 0, "items": []}

    return {"index": 0, "total": body["totalItems"], "items": book_list}
