#!/usr/bin/python3
"""Unit tests for HBNBCommand class"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand class"""

    def test_create(self):
        """Test the 'create' command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_create_unsupported_class(self):
        """Test creating an instance for an unsupported class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create UnsupportedClass")
            output = mock_stdout.getvalue()
            self.assertIn("** class doesn't exist **", output)

    def test_create_no_class_name(self):
        """Test creating an instance without specifying the class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create")
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    def test_create_instance_created_and_saved(self):
        """Test that a new instance is actually created and saved"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            instance_id = output.strip()
            obj_dict = HBNBCommand().storage.all()
            self.assertIn("BaseModel.{}".format(instance_id), obj_dict)

    def test_show(self):
        """Test the 'show' command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_show_non_existing_instance(self):
        """Test showing a non-existing instance"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_show_instance_without_class_name(self):
        """Test showing an instance without specifying the class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show")
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    def test_show_instance_without_instance_id(self):
        """Test showing an instance without specifying the instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_destroy(self):
        """Test the 'destroy' command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("destroy BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_destroy_non_existing_instance(self):
        """Test destroying a non-existing instance"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_destroy_instance_without_class_name(self):
        """Test destroying an instance without specifying the class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy")
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    def test_destroy_instance_without_instance_id(self):
        """Test destroying an instance without specifying the instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_update(self):
        """Test the 'update' command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("update BaseModel my_id name 'John'")
            HBNBCommand().onecmd("show BaseModel my_id")
            output = mock_stdout.getvalue()
            self.assertIn("John", output)

    def test_update_non_existing_instance(self):
        """Test updating an attribute of a non-existing instance"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update BaseModel non_existing_id name 'John'")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_update_instance_without_class_name(self):
        """Test updating an attribute without specifying the class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update")
            output = mock_stdout.getvalue()
            self.assertIn("** class name missing **", output)

    def test_update_instance_without_instance_id(self):
        """Test updating an attribute without specifying the instance ID"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** instance id missing **", output)

    def test_update_attribute_with_incorrect_data_type(self):
        """Test updating an attribute with an incorrect data type"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("update BaseModel my_id number_rooms 'two'")
            output = mock_stdout.getvalue()
            self.assertIn("** value must be an integer **", output)

    def test_update_invalid_attribute(self):
        """Test updating an invalid attribute"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("update BaseModel my_id invalid_attribute 'value'")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)


if __name__ == '__main__':
    unittest.main()
