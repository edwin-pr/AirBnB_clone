#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City
from tests.test_models.test_base_model import BaseModelTest

class TestCity(BaseModelTest):
    """Test the City class."""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = City

    def test_city_attributes(self):
        """Test the attributes of the City class."""
        new_city = self.test_class()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
        self.assertEqual(type(new_city.state_id), str)
        self.assertEqual(type(new_city.name), str)

    def test_str_representation(self):
        """Test the __str__ method of City."""
        new_city = self.test_class()
        str_rep = str(new_city)
        self.assertIn("[City]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict_method(self):
        """Test the to_dict method of City."""
        new_city = self.test_class()
        city_dict = new_city.to_dict()
        self.assertEqual(type(city_dict), dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)

    def test_from_dict_method(self):
        """Test creating a City instance from a dictionary."""
        new_city = self.test_class()
        city_dict = new_city.to_dict()
        city_copy = self.test_class(**city_dict)
        self.assertIsNot(city_copy, new_city)
        self.assertEqual(city_copy.to_dict(), city_dict)

    def test_city_instantiation(self):
        """Test City class instantiation with arguments and keyword arguments."""
        state_id = "state123"
        name = "Awesome City"
        city = self.test_class(state_id=state_id, name=name)
        self.assertEqual(city.state_id, state_id)
        self.assertEqual(city.name, name)

    def test_city_instantiation_override_defaults(self):
        """Test that arguments and keyword arguments override default values."""
        state_id = "state123"
        name = "Awesome City"
        kwargs = {'state_id': "state456", 'name': "Wonderful City"}
        city = self.test_class(state_id, name, **kwargs)
        self.assertEqual(city.state_id, state_id)
        self.assertEqual(city.name, name)

if __name__ == '__main__':
    unittest.main()
