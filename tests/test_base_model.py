#!/usr/bin/env python3
''' Defines unittests for models/base_model.py. '''

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    '''Unittests for the __init__ method of the BaseModel class.'''

    def test_no_args(self):
        '''Test create an instance with no arguments.'''
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(BaseModel().id), str)

    def test_unique_ids(self):
        '''Test that two instances of BaseModel have unique ids.'''
        i1 = BaseModel()
        i2 = BaseModel()
        self.assertNotEqual(i1.id, i2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = BaseModel()
        sleep(1)
        i2 = BaseModel()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = BaseModel()
        sleep(1)
        i2 = BaseModel()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        bm = BaseModel()
        bm.id = '1234567890'
        bm.created_at = dt
        bm.updated_at = dt
        expected_str = '[BaseModel] (1234567890) ' + str(bm.__dict__)
        output_str = bm.__str__()
        self.assertEqual(expected_str, output_str)


if __name__ == "__main__":
    unittest.main()
