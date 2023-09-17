#!/usr/bin/python3
'''Defines the child class - Amenity.'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Child class that represents Amenity.

    Attributes:
        name (str) - The name of the amenity.
    '''

    name = ''
