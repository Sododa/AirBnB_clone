#!/usr/bin/python3
"""writes a class Review  that inherits from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Class that defines properties of Review .basemodel
    """
    place_id = ""
    user_id = ""
    text = ""
