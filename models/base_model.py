#!/usr/bin/python3
"""writes a class Base"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class that defines base """

    def __init__(self, *args, **kwargs):
        """ definesinstances of Base """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for (key, value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """string represation of class details.
        """
        string = "["
        string += str(self.__class__.__name__) + '] ('
        string += str(self.id) + ') ' + str(self.__dict__)
        return string

    def save(self):
        """defines a save ated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ning all key/values of __dict__ of
            dict: key/value pairs.
        """
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        return dict_
