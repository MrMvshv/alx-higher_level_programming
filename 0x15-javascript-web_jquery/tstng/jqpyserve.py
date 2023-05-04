#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/0', strict_slashes=False)
def index0():
    """returns 0!"""
    return render_template('0-main.html')


@app.route('/1', strict_slashes=False)
def index1():
    """returns 1!"""
    return render_template('1-main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug = True)
