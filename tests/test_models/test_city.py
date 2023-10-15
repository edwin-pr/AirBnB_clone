#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City
from tests.test_models.test_base_model import BaseModelTest


class TestCity(BaseModelTest):
    """Test the City class"""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = City

    def test_attributes(self):
        """Test the attributes of the City class"""
        new_city = self.test_class()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
        self.assertEqual(type(new_city.state_id), str)
        self.assertEqual(type(new_city.name), str)

    def test_str(self):
        """Test the __str__ method of City"""
        new_city = self.test_class()
        str_rep = str(new_city)
        self.assertIn("[City]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict(self):
        """Test the to_dict method of City"""
        new_city = self.test_class()
        city_dict = new_city.to_dict()
        self.assertEqual(type(city_dict), dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)

    def test_from_dict(self):
        """Test creating a City instance from a dictionary"""
        new_city = self.test_class()
        city_dict = new_city.to_dict()
        city_copy = self.test_class(**city_dict)
        self.assertTrue(city_copy is not new_city)
        self.assertEqual(city_copy.to_dict(), city_dict)

    def test_args_kwargs(self):
        """Test City class instantiation with args and kwargs."""
        args = ["state123", "Awesome City"]
        city = self.test_class(*args)
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "Awesome City")

        kwargs = {'state_id': "state456", 'name': "Wonderful City"}
        city = self.test_class(**kwargs)
        self.assertEqual(city.state_id, "state456")
        self.assertEqual(city.name, "Wonderful City")

    def test_args_kwargs_override(self):
        """Test that args and kwargs override default values."""
        args = ["state123", "Awesome City"]
        kwargs = {'state_id': "state456", 'name': "Wonderful City"}
        city = self.test_class(*args, **kwargs)
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "Awesome City")

if __name__ == '__main__':
    unittest.main()
