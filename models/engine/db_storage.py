#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """This is the db storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """This shall init db Storage"""
        db_vars = {
            'host': os.getenv('HBNB_MYSQL_HOST'),
            'user': os.getenv('HBNB_MYSQL_USER'),
            'pwd': os.getenv('HBNB_MYSQL_PWD'),
            'db': os.getenv('HBNB_MYSQL_DB')
        }
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_vars['user'], db_vars['pwd'],
                                              db_vars['host'], db_vars['db']),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This shall search current db all obj depeneding on cls name"""
        nuevo_dct = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                ky = "{}.{}".format(obj.__class__.__name__, obj.id)
                nuevo_dct[ky] = obj
            else:
                for cl in [User, State, City, Place, Amenity, Review]:
                    for obj in self.__session.query(cl):
                        ky = "{}.{}".format(obj.__class__.__name__. obj.id)
                        nuevo_dct[ky] = obj
            return nuevo_dct

    def new(self, obj):
        """This shall add obj to db session"""
        self.__session.add(obj)

    def save(self):
        """This shall commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """THis shall del from db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This shall create table in db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """THis shall close session"""
        self.__session.remove()
