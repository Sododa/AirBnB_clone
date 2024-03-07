#!/usr/bin/python3
"""Public class attributes"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """define initial.
        """
        super().__init__(*args, **kwargs)
