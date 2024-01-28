#!/usr/bin/python3
""""Flask app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def f_states():
    """Render states"""
    return render_template("7-states_list.html", states=storage.all("State"))


@app.teardown_appcontext
def reload_sql():
    """Reload DB"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
