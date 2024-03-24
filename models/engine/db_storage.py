#!/usr/bin/python3
"""This shall represent DBStorage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os
from os import getenv

classes = {"State": State, "City": City, "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    """This is the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """This shall initialize the DBStorage"""
        database = "{}://{}:{}@{}:3306/{}".format("mysql+mysqldb",
                                                  getenv("HBNB_MYSQL_USER"),
                                                  getenv("HBNB_MYSQL_PWD"),
                                                  getenv("HBNB_MYSQL_HOST"),
                                                  getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(database, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This shall query objs on current database session"""
        ent = dict()
        if cls:
            return self.get_data(cls, ent)
        for ent in classes:
            self.get_data(eval(ent), ent)
        return ent

    def get_data(self, cls, st):
        """ THis shall return all objects of a class """
        cherch = self.__session.query(cls)
        for ele in cherch.all():
            cle = "{}.{}".format(cls.__name__, ele.id)
            st[cle] = ele
        return st

    def new(self, obj):
        """This shall add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This shall commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This shall delete current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This shall create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """This shall close the session"""
        self.__session.close()
