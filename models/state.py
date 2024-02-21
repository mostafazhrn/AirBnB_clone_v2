#!/usr/bin/python3
""" This code represent state Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ This shall represent the state class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """This shall init the state"""
        super().__init__(*args, **kwargs)
