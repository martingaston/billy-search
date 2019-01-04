from flask import Flask, render_template, request, redirect, url_for
from .utils import BookList


def create_app(test_config=None):
    """Create and configure Flask application factory for Billy Booksearch app"""

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

        query = request.args.get('search')
        book_list_parsed = BookList(query, start).parse()

        if len(book_list_parsed["items"]) > 0:
            return render_template("search.html", start=start+1, count=start + len(book_list_parsed["items"]), search=query, data=book_list_parsed)
        else:
            return redirect(url_for("index"))

    @app.errorhandler(404)
    def page_not_found(error):
        """Return 404 for incorrect HTTP queries"""
        return "404 - Page Not Found!", 404

    return app
