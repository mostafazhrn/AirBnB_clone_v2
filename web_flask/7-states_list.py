#!/usr/bin/python3
""" This shall start the flask web app"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This shall display the html page"""
    sts = storage.all(State).values()
    return render_template('7-states_list.html', sts=sts)


@app.teardown_appcontext
def teardown_db(exception):
    """This shall remove session sqlalchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
