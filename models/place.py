#!/usr/bin/python3
"""Defines a class Place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Attributes:
        city_id (string): id of city.
        user_id (string): id of user.
        name (string): name of Place.
        description (string): description of place.
        number_rooms (integer): number of rooms in place.
        number_bathrooms (integer): number of bathrooms in place.
        max_guest (integer): maximum number of guests allowed in a place.
        price_by_night (integer): price of room per night.
        latitude (float): latitude of place on a map.
        longitude (float): longitude of place on a map.
        amenity_ids (list (of string)): list of Amenity.id of place.
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

    def __init__(self, *args, **kwargs):
        """Creates instance
        """
        super().__init__(*args, **kwargs)
