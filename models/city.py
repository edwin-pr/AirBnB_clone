#!/usr/bin/env python3
""" city module """
from models.base_model import BaseModel

class City(BaseModel):
    """
    Attributes:
        state_id (str): The state ID to which the city belongs.
        name (str): The name of the city.
    """
    state_id = "" 
    name = ""
