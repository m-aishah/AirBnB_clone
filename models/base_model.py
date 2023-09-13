#!/usr/bin/python3
"""This defines a class"""
import uuid
import datetime

class BaseModel:
    """This class BaseModel forms the base class from which other classes will inherit"""

    def __init__(self):
        """Create an instance of the class"""
        self.id=str(uuid.uuid4())
        self.created_at=datetime.datetime.now()
        self.updated_at=datetime.datetime.now()

    def __str__(self):
        return f'{[self.__class__.__name__]} ({(self.id)}) {self.__dict__}'


if __name__ == "__main__":
    base_instance = BaseModel()
    print(base_instance)
