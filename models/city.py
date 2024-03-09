#!/usr/bin/python3
"""Public class attributes"""
from models.base_model import BaseModel


class City(BaseModel):
    """state_id: string - empty string: it will be the State.id
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """name: string - empty string
        """
        super().__init__(*args, **kwargs)
