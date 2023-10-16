#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from models.base_model import BaseModel
from tests.test_models.test_base_model import BaseModelTest
from datetime import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up for the test"""
        self.model = BaseModel()
        self.model.name = 'BaseModel'
        self.model.value = 42
        self.model.save()

    def tearDown(self):
        """Tear down after the test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default_instantiation(self):
        """Test default instantiation"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        copy = self.model.to_dict()
        new = BaseModel(**copy)
        self.assertNotEqual(new, self.model)

    def test_kwargs_with_invalid_int(self):
        """Test instantiation with invalid int kwargs"""
        copy = self.model.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save_method(self):
        """Test saving to file"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], self.model.to_dict())

    def test_str_representation(self):
        """Test string representation"""
        self.assertEqual(
            str(self.model),
            '[BaseModel] ({}) {}'.format(self.model.id, self.model.__dict__)
        )

    def test_to_dict_method(self):
        """Test to_dict method"""
        n = self.model.to_dict()
        self.assertEqual(self.model.to_dict(), n)

    def test_id_attribute(self):
        """Test ID attribute"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at_attribute(self):
        """Test created_at attribute"""
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_attribute(self):
        """Test updated_at attribute"""
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_args_instantiation(self):
        """Test instantiation with args"""
        args = [1, "Hello", 43.14]
        new = BaseModel(*args)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 43.14)

    def test_args_override_defaults(self):
        """Test args overriding default values"""
        args = [1, "Hello", 53.14]
        new = BaseModel(*args, name="World", value=2.71)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 53.14)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        kwargs = {'id': 1, 'name': "Hello", 'value': 43.14}
        new = BaseModel(**kwargs)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 43.14)

    def test_kwargs_override_defaults(self):
        """Test kwargs overriding default values"""
        kwargs = {'id': 3, 'name': "Hello", 'value': 33.14}
        new = BaseModel(id=2, name="World", value=2.71, **kwargs)
        self.assertEqual(new.id, 3)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 33.14)

if __name__ == '__main__':
    unittest.main()
