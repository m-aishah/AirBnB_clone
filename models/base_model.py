#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """Forms the base class from which other classes will inherit."""

    def __init__(self):
        """Create an instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({(self.id)}) {self.__dict__}'
