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
    """
    TestFileStorage class to test the FileStorage class methods.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the test environment."""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all() method."""
        obj1 = BaseModel()
        obj2 = Place()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objects)
        self.assertIn("Place.{}".format(obj2.id), all_objects)

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """Test the save() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload() method."""
        obj = BaseModel()
        
        """Add the object to storage"""
        self.storage.new(obj)
        
        """Save the objects to the JSON file"""
        self.storage.save()
        self.storage._FileStorage__objects = {}
        
        """Reload the objects from the JSON file"""
        self.storage.reload()
        
        """Check if the object is in the dictionary after reload"""
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

if __name__ == '__main__':
    unittest.main()
