#!/usr/bin/env python3
""" Place module """

from models.base_model import BaseModel

class Place(BaseModel):
    """
    This Place class represents a place to stay.

    Attributes:
        city_id (str): City's ID related place.
        user_id (str): The place's owner's user ID.
        name (str): The locations or places name.
        description (str): This is the place's clear description.
        number_rooms (int): The quantity of rooms avaible in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The highest number of guests the place can accommodate.
        price_by_night (int): The price per night for accomadation.
        latitude (float): The place's latitude coordinate.
        longitude (float): The places' longitude coordinate.
        amenity_ids (list): The Amenity IDs in the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
