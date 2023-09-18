#!/usr/bin/python3
'''This defines a class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class User that inherits from the BaseModel'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
