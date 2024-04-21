#!/usr/bin/python3

'''
task 8
'''

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    displays a list of cities by states.
    """
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def cl(random):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
