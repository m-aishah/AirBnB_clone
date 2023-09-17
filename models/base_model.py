#!/usr/bin/python3
'''Defines the BaseModel class.'''

import uuid
import models
from datetime import datetime


class BaseModel:
    '''Forms the base class from which other classes will inherit.'''

    def __init__(self, *args, **kwargs):
        '''Create an instance of the BaseModel class.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value pair of attributes.
        '''

        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], time_format)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], time_format)

            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __setattr__(self, name, value):
        if name != '__class__':
            super().__setattr__(name, value)

    def save(self):
        '''Updates updated_at with the current datetime.'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Return a dict representation fo an instance of BaseModel class.

        - The dict contains all the set instance attributes.
        - It also contains a key/value pair: __class__/te name of the class
        - The created_at and updated_at values will be in the iso format.'''

        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep

    def __str__(self):
        ''' Return the str/print rep of an instance of BaseModel class.'''
        return f'[{self.__class__.__name__}] ({(self.id)}) {self.__dict__}'


def main():
    # Create a dictionary representation of a BaseModel instance
    bm_dict = {
        'id': '1234567890',
        'created_at': '2023-09-13T14:30:00.000000',
        'updated_at': '2023-09-14T10:15:30.123456',
        'some_attribute': 'value'
    }

    # Initialize a BaseModel instance using the dictionary
    bm = BaseModel(**bm_dict)

    # Verify that attributes are correctly set
    print(f'id: {bm.id}')
    print(f'some_attribute: {bm.some_attribute}')

    # Verify that 'created_at' and 'updated_at' are datetime objects
    print(f'created_at: {bm.created_at}')
    print(f'updated_at: {bm.updated_at}')

if __name__ == '__main__':
    main()
