import requests


def google_book_search(search, startIndex=0, maxResults=20):
    params = {"q": search, 'startIndex': startIndex, 'maxResults': maxResults}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=params)
    return {"status": r.status_code, "body": r.json()}


def parse_search(item, results):
    return "Hello"
