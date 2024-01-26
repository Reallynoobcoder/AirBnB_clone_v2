#!/usr/bin/python3
"""Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB when /hbnb URL is accessed"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """Return C followed by input variable"""
    text_spaces = text.replace('_', ' ')
    return f"C {text_spaces}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
