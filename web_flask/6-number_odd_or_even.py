#!/usr/bin/python3

'''
task 6
'''

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return f'C {escape(text).replace("_", " ")}'


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_fun(text):
    return f'Python {escape(text).replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{escape(n)} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_o_even(n):
    return render_template("6-number_odd_or_even.html",
                           e_o="odd" if n % 2 else "even", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
