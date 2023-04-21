#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review }

    def all(self, cls=None):

        """returns a dictionary
        Return:
            returns a dictionary of __object
        """

        all_return = {}

        # if cls is valid
        if cls:
            if cls.__name__ in self.classes:
                # copy objects of cls to temp dict
                for key, val in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        all_return.update({key: val})
        else:  # if cls is none
            all_return = self.__objects

        return all_return

    def new(self, obj):

        """sets __object to given obj
        Arguments:
            obj: given object
        """

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):

        """Saves storage dictionary to file"""

        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        
        """Loads storage dictionary from file"""

        from models.engine.file_storage import FileStorage
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] =  classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    def close(self):

        """Reload JSON objects
        """

        return self.reload()

    def delete(self, obj=None):

        """delete obj from __objects if present
        """
        if obj:
            # format key from obj
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

