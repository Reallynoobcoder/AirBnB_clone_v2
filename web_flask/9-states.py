#!/usr/bin/python3
""""Flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('states/<state_id>', strict_slashes=False)
def citties_by_states(state_id=None):
    """Display the states and cities list ordered by alphabet"""
    states = storage.all(State)
    if state_id:
        state_id = f"State.{state_id}"
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def reload_sql(exeption):
    """Reload DB"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
