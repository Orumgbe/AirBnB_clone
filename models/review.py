#!/usr/bin/python3
"""Module contains the Review class object"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review class model
        Public class attribute: place_id, user_id, text
    """
    place_id = ""
    user_id = ""
    text = ""
