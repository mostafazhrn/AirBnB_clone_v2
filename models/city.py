#!/usr/bin/python3
""" This shall represent the City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state Tablename, ID , places and name """
    __tablename__ = "cities"
    satate_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities")

    def __init__(self, *args, **kwargs):
        """This shall init the city model"""
        super().__init__(*args, **kwargs)
