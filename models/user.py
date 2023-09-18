#!/usr/bin/python3
'''This defines a class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class User that inherits from the BaseModel

    Attributes:
        email (str) - The email address of the User.
        password (str) - The User's password.
        first_name (str) - The User's first name.
        last_name (str) - The User's last name.
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
