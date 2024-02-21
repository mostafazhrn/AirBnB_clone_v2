#!/usr/bin/python
""" holds class City"""
import models
import os
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities")

    def __init__(self, *args, **kwargs):
        """This shall initialize the city"""
        super().__init__(*args, **kwargs)
