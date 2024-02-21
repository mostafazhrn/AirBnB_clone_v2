#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os
import models
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This shall represent the place class"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    @property
    def reviews(self):
        """ This shall represent the getter"""
        revw_lst = []
        for revw in models.storage.all(Review).values():
            if revw.place_id == self.id:
                revw_lst.append(revw)
        return revw_lst

    @property
    def amenities(self):
        """THis shall represent getter for amenities"""
        amnty_lst = []
        for amnty in models.storage.all(Amenity).values():
            if amnty.place_id == self.id:
                amnty_lst.append(amnty)
        return amnty_lst

    @amenities.setter
    def amenities(self, obj):
        """ this shall rep setter for amenities """
        if isinstance(obj, Amenity):
            self.amenities.append(obj)
