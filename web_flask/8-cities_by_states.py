#!/usr/bin/python3
""" This script shall start the flask web app"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """This shall display the html page"""
    sts = sorted(list(storage.all(State).values()), key=lambda j: j.name)
    return render_template('8-cities_by_states.html', sts=sts)


@app.teardown_appcontext
def teardown_db(exception):
    """This shall remove session sqlalchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
