#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """This shall return the list of City instances with state_id"""
            new_list = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    new_list.append(value)
            return new_list

    def __init__(self, *args, **kwargs):
        """This shall initialize the state"""
        super().__init__(*args, **kwargs)
