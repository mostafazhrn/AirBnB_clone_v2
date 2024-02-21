#!/usr/bin/python3
"""This script shall define the base model after update"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import os

Base = declarative_base()


class BaseModel:
    """This shall represent the base model class updated """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This shall instatntiates the updated model"""
        if kwargs:
            for cle, valu in kwargs.items():
                if cle == "created_at" or cle == "updated_at":
                    valu = datetime.strptime(valu, "%Y-%m-%dT%H:%M:%S.%f")
                    if cle != "__class__":
                        setattr(self, cle, valu)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            temp = datetime.now()
            if "created_at" not in kwargs:
                self.created_at = temp
                if "updated_at" not in kwargs:
                    self.updated_at = time
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        mi_dct = self.__dict__.copy()
        mi_dct["__class__"] = self.__class__.__name__
        mi_dct["created_at"] = self.created_at.isoformat()
        mi_dct["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in mi_dct:
            del mi_dct["_sa_instance_state"]
        return mi_dct

    def delete(self):
        """This shall del instance from storage"""
        models.storage.delete(self)
