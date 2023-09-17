#!/usr/bin/python3
'''Defines a child class - Review.'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Child class that represents Review.

    Attributes:
        place_id (str) - The Place id.
        user_id (str) - The User id.
        text (str) - A review of the place.
    '''

    place_id = ''
    user_id = ''
    text = ''
