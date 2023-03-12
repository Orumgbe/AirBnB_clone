#!/usr/bin/python3
"""Module contains the City class object"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines City class model
        Public class attributes: name, state_id
    """
    name = ""
    state_id = ""
