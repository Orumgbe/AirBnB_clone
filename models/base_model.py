#!/usr/bin/python3
"""Module defines the BaseModel class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for all models of hbnb clone"""
    def __init__(self, *args, **kwargs):
        """Initialization of a new model object"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            del(kwargs['__class__'])
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

    def __str__(self):
        """Return string representation of instance created"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates public instance attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all information of the instance"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({'__class__': type(self).__name__})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
