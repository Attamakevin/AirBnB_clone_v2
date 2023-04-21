#!/usr/bin/python3
<<<<<<< HEAD
"""Create a unique storage instance for your application"""
=======
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
>>>>>>> d26c8ad4422b53fba87eeed2f18cf2244a49fd77

from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

<<<<<<< HEAD
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
=======
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
>>>>>>> d26c8ad4422b53fba87eeed2f18cf2244a49fd77
