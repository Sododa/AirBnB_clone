#!/usr/bin/python3
""" classes that inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """classes that inherit from BaseModel
        """
        super().__init__(*args, **kwargs)
