#!/usr/bin/env python3
""" state module """
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that represents a state and inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
