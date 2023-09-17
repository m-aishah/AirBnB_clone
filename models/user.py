#!/usr/bin/python3
'''This defines a class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class User that inherits from the BaseModel'''

    def __init__(self):
        '''Initialising an instace of the class User'''

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
