#!/usr/bin/python3
""" THis shall represent the State class for airbnb_clone_v2 """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer


class State(BaseModel, Base):
    """ This shall represent the State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            """ this shall return list of cities instances"""
            cities = list()
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
