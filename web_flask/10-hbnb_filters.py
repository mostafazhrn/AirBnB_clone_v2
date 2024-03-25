#!/usr/bin/python3
""" This script shall start the flask web app"""
from flask import Flask, render_template, url_for
from models import storage
from models import *
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ This shall display the html page"""
    stts = storage.all(State).values()
    cities = list()
    amenits = storage.all(Amenity).values()

    for stt in stts:
        for city in stt.cities:
            cities.append(city)
    return render_template('10-hbnb_filters.html', stts=stts,
                           cities=cities, amenits=amenits)


@app.teardown_appcontext
def teardown_db(exception):
    """This shall remove session sqlalchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
