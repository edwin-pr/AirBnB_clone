#!/usr/bin/env python3
"""This is a representation of a user and inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that represents a user and inherits from BaseModel.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
