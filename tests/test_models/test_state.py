#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State
from tests.test_models.test_base_model import BaseModelTest


class TestState(BaseModelTest):
    """Test the State class"""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = State

    def test_attributes(self):
        """Test the attributes of the State class"""
        new_state = self.test_class()
        self.assertTrue(hasattr(new_state, 'name'))
        self.assertEqual(new_state.name, "")
        self.assertEqual(type(new_state.name), str)

    def test_str(self):
        """Test the __str__ method of State"""
        new_state = self.test_class()
        str_rep = str(new_state)
        self.assertIn("[State]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict(self):
        """Test the to_dict method of State"""
        new_state = self.test_class()
        state_dict = new_state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_from_dict(self):
        """Test creating a State instance from a dictionary"""
        new_state = self.test_class()
        state_dict = new_state.to_dict()
        state_copy = self.test_class(**state_dict)
        self.assertTrue(state_copy is not new_state)
        self.assertEqual(state_copy.to_dict(), state_dict)

    def test_name3(self):
        """Test the 'name' attribute of the State class"""
        new_state = self.test_class()
        self.assertEqual(type(new_state.name), str)
        
    def test_args_kwargs(self):
        """Test State class instantiation with args and kwargs."""
        args = [1, "California"]
        state = self.test_class(*args)
        self.assertEqual(state.id, 1)
        self.assertEqual(state.name, "California")

        kwargs = {'id': 2, 'name': "Texas"}
        state = self.test_class(**kwargs)
        self.assertEqual(state.id, 2)
        self.assertEqual(state.name, "Texas")

    def test_args_kwargs_override(self):
        """Test that args and kwargs override default values."""
        args = [1, "California"]
        kwargs = {'id': 2, 'name': "Texas"}
        state = self.test_class(*args, **kwargs)
        self.assertEqual(state.id, 1)  # Args override kwargs
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
