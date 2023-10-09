#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test the __init__ method for creating a new instance
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        # Test the __str__ method
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        # Test the save method
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_new(self):
        # Test the new method in FileStorage (assuming FileStorage works correctly)
        obj = BaseModel()
        self.assertIn("BaseModel.{}".format(obj.id), storage.all())

if __name__ == '__main__':
    unittest.main()
