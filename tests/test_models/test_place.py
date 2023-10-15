#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from models.place import Place
from tests.test_models.test_base_model import BaseModelTest


class TestPlace(BaseModelTest):
    """Test the Place class"""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = Place

    def test_attributes(self):
        """Test the attributes of the Place class"""
        new_place = self.test_class()
        self.assertTrue(hasattr(new_place, 'city_id'))
        self.assertTrue(hasattr(new_place, 'user_id'))
        self.assertTrue(hasattr(new_place, 'name'))
        self.assertTrue(hasattr(new_place, 'description'))
        self.assertTrue(hasattr(new_place, 'number_rooms'))
        self.assertTrue(hasattr(new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(new_place, 'max_guest'))
        self.assertTrue(hasattr(new_place, 'price_by_night'))
        self.assertTrue(hasattr(new_place, 'latitude'))
        self.assertTrue(hasattr(new_place, 'longitude'))
        self.assertTrue(hasattr(new_place, 'amenity_ids'))
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])
        self.assertEqual(type(new_place.city_id), str)
        self.assertEqual(type(new_place.user_id), str)
        self.assertEqual(type(new_place.name), str)
        self.assertEqual(type(new_place.description), str)
        self.assertEqual(type(new_place.number_rooms), int)
        self.assertEqual(type(new_place.number_bathrooms), int)
        self.assertEqual(type(new_place.max_guest), int)
        self.assertEqual(type(new_place.price_by_night), int)
        self.assertEqual(type(new_place.latitude), float)
        self.assertEqual(type(new_place.longitude), float)
        self.assertEqual(type(new_place.amenity_ids), list)

    def test_str(self):
        """Test the __str__ method of Place"""
        new_place = self.test_class()
        str_rep = str(new_place)
        self.assertIn("[Place]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict(self):
        """Test the to_dict method of Place"""
        new_place = self.test_class()
        place_dict = new_place.to_dict()
        self.assertEqual(type(place_dict), dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)

    def test_from_dict(self):
        """Test creating a Place instance from a dictionary"""
        new_place = self.test_class()
        place_dict = new_place.to_dict()
        place_copy = self.test_class(**place_dict)
        self.assertTrue(place_copy is not new_place)
        self.assertEqual(place_copy.to_dict(), place_dict)

    def test_args_kwargs(self):
        """Test Place class instantiation with args and kwargs."""
        args = ["city123", "user456", "Beautiful Place"]
        place = self.test_class(*args)
        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user456")
        self.assertEqual(place.name, "Beautiful Place")

        kwargs = {
            'city_id': "city789",
            'user_id': "user101",
            'name': "Awesome Place"
        }
        place = self.test_class(**kwargs)
        self.assertEqual(place.city_id, "city789")
        self.assertEqual(place.user_id, "user101")
        self.assertEqual(place.name, "Awesome Place")

    def test_args_kwargs_override(self):
        """Test that args and kwargs override default values."""
        args = ["city123", "user456", "Beautiful Place"]
        kwargs = {
            'city_id': "city789",
            'user_id': "user101",
            'name': "Awesome Place"
        }
        place = self.test_class(*args, **kwargs)
        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user456")
        self.assertEqual(place.name, "Beautiful Place")

if __name__ == '__main__':
    unittest.main()
