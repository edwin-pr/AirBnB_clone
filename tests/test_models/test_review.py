#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review
from tests.test_models.test_base_model import BaseModelTest


class TestReview(BaseModelTest):
    """Test the Review class"""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = Review

    def test_attributes(self):
        """Test the attributes of the Review class"""
        new_review = self.test_class()
        self.assertTrue(hasattr(new_review, 'place_id'))
        self.assertTrue(hasattr(new_review, 'user_id'))
        self.assertTrue(hasattr(new_review, 'text'))
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")
        self.assertEqual(type(new_review.place_id), str)
        self.assertEqual(type(new_review.user_id), str)
        self.assertEqual(type(new_review.text), str)

    def test_str(self):
        """Test the __str__ method of Review"""
        new_review = self.test_class()
        str_rep = str(new_review)
        self.assertIn("[Review]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict(self):
        """Test the to_dict method of Review"""
        new_review = self.test_class()
        review_dict = new_review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_from_dict(self):
        """Test creating a Review instance from a dictionary"""
        new_review = self.test_class()
        review_dict = new_review.to_dict()
        review_copy = self.test_class(**review_dict)
        self.assertTrue(review_copy is not new_review)
        self.assertEqual(review_copy.to_dict(), review_dict)

    def test_args_kwargs(self):
        """Test Review class instantiation with args and kwargs."""
        args = ["123", "456", "Great place"]
        review = self.test_class(*args)
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place")

        kwargs = {'place_id': "789", 'user_id': "101", 'text': "Awesome"}
        review = self.test_class(**kwargs)
        self.assertEqual(review.place_id, "789")
        self.assertEqual(review.user_id, "101")
        self.assertEqual(review.text, "Awesome")

    def test_args_kwargs_override(self):
        """Test that args and kwargs override default values."""
        args = ["123", "456", "Great place"]
        kwargs = {'place_id': "789", 'user_id': "101", 'text': "Awesome"}
        review = self.test_class(*args, **kwargs)
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place")


if __name__ == '__main__':
    unittest.main()
