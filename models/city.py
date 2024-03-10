#!/usr/bin/python3
"""writes a class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that writes a properties of City.
    """
    state_id = ""
    name = ""
