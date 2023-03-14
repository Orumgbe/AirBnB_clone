#!/usr/bin/python3
"""This module defines class 'FileStorage' to manage storage for hbnb clone"""
import json


class FileStorage:
    """Serializes and deserializes instances using JSON"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Updates '__objects' dictionary with new obj"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serializes __objects to json file"""
        temp = {}
        temp.update(FileStorage.__objects)
        for k, v in temp.items():
            temp[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp, f)

    def reload(self):
        """Deserializes json file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as rf:
                temp = json.load(rf)
            for key, val in temp.items():
                self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
