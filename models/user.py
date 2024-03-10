#!/usr/bin/python3
"""writes a class User  inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines properties for basemodel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
