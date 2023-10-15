#!/usr/bin/python3
""" review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review and inherits from BaseModel.

    Attributes:
        place_id (str): Ths representss the place's ID
        user_id (str): This represents the reviewer's ID
        text (str): This represents the textual content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
