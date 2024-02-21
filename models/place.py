#!/usr/bin/python3
""" THis is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """THis shall rep place class"""
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="delete")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """ This shall rep the getter of reviews"""
            lst_revws = []
            all_revws = models.storage.all(Review)
            for revew in all_revws.values():
                if revew.place_id == self.id:
                    lst_revws.append(revew)
            return lst_revws

        @property
        def amenities(self):
            """this shall rep the getter amenities"""
            lst_amen = []
            all_amen = models.storage.all(Amenity)
            for amen in all_amen:
                if amen.place_id == self.id:
                    lst_amen.append(amen)
            return lst_amen

        @amenities.setter
        def amenities(self, obj):
            """ THis shall rep setter of amenity ids"""
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
            else:
                pass
