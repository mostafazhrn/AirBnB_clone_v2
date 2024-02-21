#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """ This shall rep the Amenity class for MySQL db"""
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ""
        place_amenities = []

        @property
        def place_amenities(self):
            """This shall rep the getter of amenities"""
            lst_amen = []
            all_amen = models.storage.all(Amenity)
            for amen in all_amen:
                if amen.place_id == self.id:
                    lst_amen.append(amen)
            return lst_amen

        @place_amenities.setter
        def place_amenities(self, obj):
            """This shall rep the setter for amenities"""
            if type(obj) is Place:
                self.place_amenities.append(obj.id)
            else:
                pass
