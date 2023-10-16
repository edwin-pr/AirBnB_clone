#!/usr/bin/python3
"""Test the FileStorage class methods."""
import unittest
import os
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class methods."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment."""
        cls.storage = FileStorage()
        cls.storage.reload()  # Load any existing data

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        """Test the all() method."""
        obj1 = BaseModel()
        obj2 = Place()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objects)
        self.assertIn("Place.{}".format(obj2.id), all_objects)

    def test_new_method(self):
        """Test the new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save_method(self):
        """Test the save() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        """Test the reload() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

if __name__ == '__main__':
    unittest.main()
