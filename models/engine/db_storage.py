#!/usr/bin/python3
<<<<<<< HEAD
"""This is storage engine using MySQL database
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """This class manages MySQL storage using SQLAlchemy
    Attributes:
        __engine: engine object
        __session: session object
    """
=======
"""This module defines a class to handle Database storage"""
import os
from sqlalchemy import create_engine, inspect, Column, Integer
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class provides blueprints for objects that can interact
    with a MySQL db"""
>>>>>>> d26c8ad4422b53fba87eeed2f18cf2244a49fd77
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Create SQLAlchemy engine
        """
        # creating engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop tables if test is equal to environment
        if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query and return all objects by class/generally
        Return: dictionary (<class-name>.<object-id>: <obj>)
        """
        obj_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                # populate dict with objects from storage
                obj_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database session
        """
        if obj:
            # determine class from obj
            cls_name = classes[type(obj).__name__]

            # query class table and delete
            self.__session.query(cls_name).\
                filter(cls_name.id == obj.id).delete()

    def reload(self):
        """Create database session
        """
        # create session from current engine
        Base.metadata.create_all(self.__engine)
        # create db tables
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        # from previousy:
        # Session = scoped_session(session)
        self.__session = scoped_session(session)

    def close(self):
        """Close scoped session
        """
        self.__session.remove()
=======
        """Initializes the DBStorage engine object"""
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"), os.getenv(
                "HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"))

        DBStorage.__engine = create_engine(url, pool_pre_ping=True)
        # Drop all tables if in test mode
        if os.getenv("HBNB_ENV") == "test":
            with DBStorage.__engine.connect() as conn:
                for table in ['reviews', 'place_amenity', 'places',
                              'cities', 'states', 'amenities', 'users']:
                    conn.execute(
                        "DROP TABLE IF EXISTS {}".format(table))

    def all(self, cls=None):
        """
        all returns all instance of the given class from the database
        if cls is None it returns all objects stored in the database

        :param cls: is the class of object to retrieve from the database
        :return: is a dictionary of objects ids to object values
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        objects = {}
        if cls is None:
            classes = [City, State, Place, Amenity, Review, User]
            for clas in classes:
                for obj in DBStorage.__session.query(clas):
                    objects["{}.{}".format(clas.__name__, obj.id)] = obj
        else:
            for obj in DBStorage.__session.query(cls):
                objects["{}.{}".format(cls.__name__, obj.id)] = obj
        return objects

    def new(self, obj):
        """
        new adds the given object into the current database session

        :param obj: is the object to be add the current database session
        """
        DBStorage.__session.add(obj)

    def save(self):
        """
        save commits the current session to the database
        """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """
        delete removes an instance from the current session if not None

        :param obj: is the object instance to remove from the current session
        """
        if obj is not None:
            DBStorage.__session.delete(obj)
            self.save()

    def reload(self):
        """
        reload creates all tables if necessary and assign a database
        session object to the private class attribute __session
        """
        from models.base_model import Base, BaseModel
        from models.city import City
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(DBStorage.__engine)
        DBStorage.__session = sessionmaker(
            bind=DBStorage.__engine, expire_on_commit=False)()

    def close(self):
        """Closes the storage engine."""
        self.__session.close()
>>>>>>> d26c8ad4422b53fba87eeed2f18cf2244a49fd77
