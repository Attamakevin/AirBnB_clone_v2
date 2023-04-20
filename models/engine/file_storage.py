#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import re


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

<<<<<<< HEAD
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items(
        ) if re.match("^{}\\..*".format(cls.__name__), k)}
=======
    classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}

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
>>>>>>> b9bac4719f8c40b10aee401a1c7ae6dd816f867e

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
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
<<<<<<< HEAD

    def delete(self, obj=None):
        """
        delete removes the instance obj is not None from the private class
        attribute __objects

        :param obj: is the object to be removed
        """
        if obj is None:
            return
        id = "{}.{}".format(obj.__class__.__name__, obj.id)
        del FileStorage.__objects[id]
        self.save()

    def close(self):
        """TODO: Docstring for close.

        :returns: TODO

        """
        self.reload()
=======
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

>>>>>>> b9bac4719f8c40b10aee401a1c7ae6dd816f867e
