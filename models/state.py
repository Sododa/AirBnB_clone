#!/usr/bin/python3
"""writes a class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that defines properties of State. basemodel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """defines a new instances of State.
        """
        super().__init__(*args, **kwargs)
