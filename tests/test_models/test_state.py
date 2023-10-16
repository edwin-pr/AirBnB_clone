#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State
from tests.test_models.test_base_model import BaseModelTest

class TestState(BaseModelTest):
    """Test the State class."""

    def setUp(self):
        """Set up for the test"""
        super().setUp()
        self.test_class = State

    def test_state_attributes(self):
        """Test the attributes of the State class."""
        new_state = self.test_class()
        self.assertTrue(hasattr(new_state, 'name'))
        self.assertEqual(new_state.name, "")
        self.assertEqual(type(new_state.name), str)

    def test_str_representation(self):
        """Test the __str__ method of State."""
        new_state = self.test_class()
        str_rep = str(new_state)
        self.assertIn("[State]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict_method(self):
        """Test the to_dict method of State."""
        new_state = self.test_class()
        state_dict = new_state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_from_dict_method(self):
        """Test creating a State instance from a dictionary."""
        new_state = self.test_class()
        state_dict = new_state.to_dict()
        state_copy = self.test_class(**state_dict)
        self.assertIsNot(state_copy, new_state)
        self.assertEqual(state_copy.to_dict(), state_dict)

    def test_name_attribute(self):
        """Test the 'name' attribute of the State class."""
        new_state = self.test_class()
        self.assertEqual(type(new_state.name), str)

    def test_state_instantiation(self):
        """Test State class instantiation with arguments and keyword arguments."""
        id_value = 1
        name = "California"
        state = self.test_class(id=id_value, name=name)
        self.assertEqual(state.id, id_value)
        self.assertEqual(state.name, name)

    def test_state_instantiation_override_defaults(self):
        """Test that arguments and keyword arguments override default values."""
        id_value = 1
        name = "California"
        kwargs = {'id': 2, 'name': "Texas"}
        state = self.test_class(id=id_value, name=name, **kwargs)
        self.assertEqual(state.id, id_value)
        self.assertEqual(state.name, name)

if __name__ == '__main__':
    unittest.main()
