#!/usr/bin/python3
'''Defines a new class called FileStorage.'''

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Serializes/desirializes instances of BaseModel class
            to/from a JSON file.

    Attributes:
        __file_path (str): Path to JSON file (ex: file.json)
        __objects (dict): Container for objects with key <class name>.id
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects.'''
        return FileStorage.__objects

    def new(self, obj):
        '''Stores an object in the __objects dictionary.

        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (any): The object to be stored.
        '''

        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file.'''
        # Convert the values of __objects to dictionaries.
        objects = FileStorage.__objects
        objects_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}
        # JSON dump into the file
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        '''Desirializes JSON file to __objects.

        If the file path does not exist, does nothing.
        '''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
