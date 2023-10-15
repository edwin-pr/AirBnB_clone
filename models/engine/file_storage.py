#!/usr/bin/env python3
"""This module aids in serialization and deserialization of objects
It also creates, saves, reloads the given objects.
"""
import json
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    FileStorage class to manage JSON serialization and
    deserialization of objects.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects from __objects dictionary.

        Returns:
            dict: A dictionary of all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize and save objects to the JSON file.
        """
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserialize and reload objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                classes = {
                    "BaseModel": BaseModel,
                    "Place": Place,
                    "Amenity": Amenity,
                    "City": City,
                    "Review": Review,
                    "State": State,
                    "User": User
                }
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in classes:
                        instance = classes[class_name](**value)
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
