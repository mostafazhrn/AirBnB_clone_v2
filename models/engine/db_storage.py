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
    """This is the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """This shall initialize the DBStorage"""
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
        """This shall query on the current database session all objects depending of the class name"""
        nuevo_dct = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                ky = "{}.{}".format(obj.__class__.__name__, obj.id)
                nuevo_dct[ky] = obj
        else:
            for cl in [User, State, City, Place, Amenity, Review]:
                for obj in self.__session.query(cl):
                    ky = "{}.{}".format(obj.__class__.__name__, obj.id)
                    nuevo_dct[ky] = obj
        return nuevo_dct
    
    def new(self, obj):
        """This shall add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This shall commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This shall delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This shall create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """This shall close the session"""
        self.__session.remove()
