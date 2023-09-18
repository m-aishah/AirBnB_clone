#!/usr/bin/python3
'''Defines the child class - City.'''

from models.base_model import BaseModel


class City(BaseModel):
    '''Child class that repesents city.

    Attributes:
        state_id (str): The State's id.
        name (str): The name of the city.
    '''

    state_id = ''
    name = ''
