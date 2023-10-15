#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import BaseModelTest


class TestAmenity(BaseModelTest):
    """Test the Amenity class"""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = Amenity

    def test_attributes(self):
        """Test the attributes of the Amenity class"""
        new_amenity = self.test_class()
        self.assertTrue(hasattr(new_amenity, 'name'))
        self.assertEqual(new_amenity.name, "")
        self.assertEqual(type(new_amenity.name), str)

    def test_str(self):
        """Test the __str__ method of Amenity"""
        new_amenity = self.test_class()
        str_rep = str(new_amenity)
        self.assertIn("[Amenity]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict(self):
        """Test the to_dict method of Amenity"""
        new_amenity = self.test_class()
        amenity_dict = new_amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(type(amenity_dict['created_at']), str)
        self.assertEqual(type(amenity_dict['updated_at']), str)

    def test_from_dict(self):
        """Test creating an Amenity instance from a dictionary"""
        new_amenity = self.test_class()
        amenity_dict = new_amenity.to_dict()
        amenity_copy = self.test_class(**amenity_dict)
        self.assertTrue(amenity_copy is not new_amenity)
        self.assertEqual(amenity_copy.to_dict(), amenity_dict)


if __name__ == '__main__':
    unittest.main()
