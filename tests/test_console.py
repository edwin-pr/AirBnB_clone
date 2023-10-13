#!/usr/bin/python3
""" testt for  console.py """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("destroy BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertIn("** no instance found **", output)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("update BaseModel my_id name 'John'")
            HBNBCommand().onecmd("show BaseModel my_id")
            output = mock_stdout.getvalue()
            self.assertIn("John", output)

if __name__ == '__main__':
    unittest.main()

