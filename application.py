from helpers import google_book_search, parse_search
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET"""
    return render_template("index.html")


@app.route('/query')
def query():
    """Display search requests and pagination via GET"""
    # return the user to the index page if they're not searching for anything
    if not request.args.get("search"):
        return redirect(url_for("index"))

    # check for correct pagination from start value
    if request.args.get("start") is None or int(request.args.get("start")) < 0:
        start = 0
    else:
        start = int(request.args.get("start"))

    # Get the search value from the request query string
    query = request.args.get('search')
    # Hit and parse the API
    api_search = google_book_search(query, start)
    parsed_text = parse_search(api_search)

    if len(parsed_text["items"]) > 0:
        return render_template("search.html", start=start+1, count=start + len(parsed_text["items"]), search=query, data=parsed_text)
    else:
        print("Items is 0!")
        return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    """Return 404 for incorrect HTTP queries"""
    return "404 - Page Not Found!", 404
