#!/usr/bin/python3
"""from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """
        place_id (string): id of ci
        text (string): just a text.
    """
    place_id = ""
    user_id = ""
    text = ""
