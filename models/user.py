#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates instance.
        """
        super().__init__(*args, **kwargs)
