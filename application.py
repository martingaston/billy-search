from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found!"
