from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return "Billy Booksearch!"


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found!"
