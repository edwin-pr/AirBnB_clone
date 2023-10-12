#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
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
