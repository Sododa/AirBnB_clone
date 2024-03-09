#!/usr/bin/python3
"""writes a class FileStorage.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Class that serializes instances to a JSON file and file storage.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates new instances self class
        """
        pass

    def all(self):
        """Returns the dictionary objects self defination
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class self obj
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file th).
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(dictionary, myFile)

    def reload(self):
        """Deserializes the JSON file reload self
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except Exception:
            return
        objects = eval(my_obj_dump)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects

    def delete(self, obj):
        """Deletes obj from self objective
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False
