#!/usr/bin/python3
'''Defines the BaseModel class.'''

import uuid
from datetime import datetime


class BaseModel:
    '''Forms the base class from which other classes will inherit.'''

    def __init__(self):
        '''Create an instance of the BaseModel class.'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''Updates updated_at with the current datetime.'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Return a dict representation fo an instance of BaseModel class.

        - The dict contains all the set instance attributes and a key/value pair:
            __class__/te name of the class
        - The created_at and updated_at values will be in the iso format.'''

        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep

    def __str__(self):
        ''' Return the str/print representation of an instance of BaseModel class.'''
        return f'[{self.__class__.__name__}] ({(self.id)}) {self.__dict__}'
