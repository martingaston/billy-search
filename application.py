from helpers import google_book_search, parse_search
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")


@app.route('/query')
def query():
    if request.args.get('search') is None:
        return redirect(url_for("/"))

    if request.args.get('start') is None or int(request.args.get('start')) < 0:
        start = 0
    else:
        start = int(request.args.get('start'))

    query = request.args.get('search')
    api_search = google_book_search(query, start)
    parsed_text = parse_search(api_search)
    return render_template("search.html", start=start+1, count=start + len(parsed_text["items"]), search=query, data=parsed_text)


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found!", 404
