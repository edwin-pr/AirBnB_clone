#!/usr/bin/python3
""" Amenity module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
   This class represents an amenity and inherits from BaseModel.

    Attributes:
        name (str): The amenity's name.
    """
    name = ""
