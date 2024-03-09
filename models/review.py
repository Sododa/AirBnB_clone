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

    def __init__(self, *args, **kwargs):
        """Creates instance for arguments.
        """
        super().__init__(*args, **kwargs)
