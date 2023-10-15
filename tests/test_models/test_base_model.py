#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from models.base_model import BaseModel
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes <--test variables"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up for the test"""
        pass

    def tearDown(self):
        """Tear down after the test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default <--instantiation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation with invalid<-- int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test saving to file"""
        i = self.value()
        i.save()
        key = "{}.{}".format(self.name, i.id)
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_to_dict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instantiation with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instantiation with single-key<-- kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test ID attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_args(self):
        """Test instantiation with args"""
        args = [1, "Hello", 43.14]
        new = self.value(*args)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 43.14)

    def test_args_override(self):
        """Test args overriding default values"""
        args = [1, "Hello", 53.14]
        new = self.value(*args, id=2, name="World", value=2.71)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 53.14)

    def test_kwargs(self):
        """Test instantiation with kwargs<--"""
        kwargs = {'id': 1, 'name': "Hello", 'value': 43.14}
        new = self.value(**kwargs)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 43.14)

    def test_kwargs_override(self):
        """Test kwargs overriding<-- default values"""
        kwargs = {'id': 3, 'name': "Hello", 'value': 33.14}
        new = self.value(id=2, name="World", value=2.71, **kwargs)
        self.assertEqual(new.id, 3)
        self.assertEqual(new.name, "Hello")
        self.assertEqual(new.value, 33.14)


if __name__ == '__main__':
    unittest.main()
