#!/usr/bin/python3
"""Unit tests for User class."""
import unittest
from models.user import User
from tests.test_models.test_base_model import BaseModelTest

class TestUser(BaseModelTest):
    """Test the User class."""

    def setUp(self):
        """Set up for the test."""
        super().setUp()
        self.test_class = User

    def test_user_attributes(self):
        """Test the attributes of the User class."""
        new_user = self.test_class()
        self.assertTrue(hasattr(new_user, 'first_name'))
        self.assertTrue(hasattr(new_user, 'last_name'))
        self.assertTrue(hasattr(new_user, 'email'))
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(type(new_user.first_name), str)
        self.assertEqual(type(new_user.last_name), str)
        self.assertEqual(type(new_user.email), str)
        self.assertEqual(type(new_user.password), str)

    def test_str_representation(self):
        """Test the __str__ method of User."""
        new_user = self.test_class()
        str_rep = str(new_user)
        self.assertIn("[User]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

    def test_to_dict_method(self):
        """Test the to_dict method of User."""
        new_user = self.test_class()
        user_dict = new_user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)


    def test_from_dict_method(self):
        """Test creating a User instance from a dictionary."""
        new_user = self.test_class()
        user_dict = new_user.to_dict()
        user_copy = self.test_class(**user_dict)
        self.assertIsNot(user_copy, new_user)
        self.assertEqual(user_copy.to_dict(), user_dict)

    def test_first_name_attribute(self):
        """Test the 'first_name' attribute of the User class."""
        new_user = self.test_class()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name_attribute(self):
        """Test the 'last_name' attribute of the User class."""
        new_user = self.test_class()
        self.assertEqual(type(new_user.last_name), str)

    def test_email_attribute(self):
        """Test the 'email' attribute of the User class."""
        new_user = self.test_class()
        self.assertEqual(type(new_user.email), str)

    def test_password_attribute(self):
        """Test the 'password' attribute of the User class."""
        new_user = self.test_class()
        self.assertEqual(type(new_user.password), str)

    def test_first_name_initial_value(self):
        """Test that 'first_name' attribute has the initial value."""
        new_user = self.test_class()
        self.assertEqual(new_user.first_name, "")

    def test_last_name_initial_value(self):
        """Test that 'last_name' attribute has the initial value."""
        new_user = self.test_class()
        self.assertEqual(new_user.last_name, "")

    def test_email_initial_value(self):
        """Test that 'email' attribute has the initial value."""
        new_user = self.test_class()
        self.assertEqual(new_user.email, "")

    def test_password_initial_value(self):
        """Test that 'password' attribute has the initial value."""
        new_user = self.test_class()
        self.assertEqual(new_user.password, "")

    def test_user_instantiation(self):
        """Test User class instantiation with arguments and keyword arguments."""
        id_value = 1
        first_name = "John"
        last_name = "Doe"
        email = "john@example.com"
        password = "password"
        user = self.test_class(id=id_value, first_name=first_name, last_name=last_name, email=email, password=password)
        self.assertEqual(user.id, id_value)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)

    def test_user_instantiation_override_defaults(self):
        """Test that arguments and keyword arguments override default values."""
        id_value = 1
        first_name = "John"
        last_name = "Doe"
        email = "john@example.com"
        password = "password"
        kwargs = {'id': 2, 'first_name': "Jane", 'last_name': "Smith", 'email': "jane@example.com", 'password': "another_password"}
        user = self.test_class(id=id_value, first_name=first_name, last_name=last_name, email=email, password=password, **kwargs)
        self.assertEqual(user.id, id_value)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)

if __name__ == '__main__':
    unittest.main()
