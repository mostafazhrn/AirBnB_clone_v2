#!/usr/bin/python3
""" This script shall start the flask web app"""
from flask import Flask, render_template
from models import storage
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ THis shall display html page with states in it"""
    stts = storage.all(State).values()
    return render_template('7-states_list.html', stts=stts)


@app.route('/states/<id>', strict_slashes=False)
def states_defined(id):
    """THis shall display the HTML page when stt id"""
    stts = storage.all(State).values()
    for stt in stts:
        if stt.id == id:
            return render_template('9-states.html', stt=stt,
                                   stt_cities=stt.cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """This shall remove session sqlalchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
