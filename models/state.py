#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            from models import storage
            from models.city import City
            # return list of City objs in __objects
            cities_dict = storage.all(City)
            citiesList = []

            # copy values from dict to list
            for city in cities_dict.values():
                if city.state_id == self.id:
                    citiesList.append(city)

            return citiesList
=======
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from models import storage
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', back_populates="state")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    City.state = relationship('State', back_populates="cities")
>>>>>>> d26c8ad4422b53fba87eeed2f18cf2244a49fd77
