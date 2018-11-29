from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
    print(request.form['query'])
    return "Ok!"


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found!", 404
