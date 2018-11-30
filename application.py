from helpers import google_book_search, parse_search
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
    query = request.form['search']
    api_search = google_book_search(query)
    parsed_text = parse_search(api_search)
    return render_template("search.html", search=query, data=parsed_text)


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found!", 404
