#!/usr/bin/python3
"""This shall represent the BaseModel class for airbnb_clone_v2"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """ This is the base model class for all other classes """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ THis shall start the base mosel class"""
        if kwargs:
            for cle, valu in kwargs.items():
                if cle == "created_at" or cle == "updated_at":
                    valu = datetime.strptime(valu, "%Y-%m-%dT%H:%M:%S.%f")
                if cle != "__class__":
                    setattr(self, cle, valu)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "created_at" in kwargs and "updated_at" not in kwargs:
                self.updated_at = self.created_at
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ This shall return the string representation of the BaseModel class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ This shall update the updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ This shall return a dictionary representation of the BaseModel class """
        mi_dict = dict(self.__dict__)
        mi_dict["__class__"] = str(type(self).__name__)
        mi_dict["created_at"] = self.created_at.isoformat()
        mi_dict["updated_at"] = self.updated_at.isoformat()
        if mi_dict["_sa_instance_state"]:
            del mi_dict["_sa_instance_state"]
        return mi_dict
    
    def delete(self):
        """ This shall delete the current instance from storage """
        models.storage.delete(self)

    def __repr__(self):
        """ This shall return the string representation of the BaseModel class """
        return self.__str__()
