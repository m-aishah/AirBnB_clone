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


class TestBaseModel_str(unittest.TestCase):
    '''Unittests for the __str__ method of the BaseModel class.'''

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


class TestBaseModel_save(unittest.TestCase):
    '''Unittests for the __save__ method of the BaseModel class.'''

    def test_save_updated_at(self):
        '''Test if save updates the updated_at time'''
        i1 = BaseModel()
        up_time_1 = i1.updated_at
        sleep(1)
        i1.save()
        up_time_2 = i1.updated_at
        self.assertNotEqual(up_time_1, up_time_2)
        self.assertLess(up_time_1, up_time_2)


class TestBaseModel_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the BaseModel class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        bm = BaseModel()
        bm.id = '1234567890'
        result = bm.to_dict()
        self.assertEqual(type(result, dict))

    def test_class_name(self):
        '''Tests if __class__ key is added with the class name'''

        bm = BaseModel()
        bm.id = '1234567890'
        result = bm.to_dict()
        self.assertEqual(result['__class__'], 'MyClass')

    def test_to_dict_output(self):
        '''Tests if created_at and updated_at are datetime objects'''
        dt = datetime.now()
        bm = BaseModel()
        bm.id = '1234567890'
        bm_dict = bm.to_dict()
        bm.created_at = dt
        bm.updated_at = dt
        bm_dict = bm.to_dict()
        self.assertEqual(type(bm_dict['created_at'], str))
        self.assertEqual(type(bm_dict['updated_at'], str))

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        bm = BaseModel()
        bm.id = '1234567890'
        initial_dict = bm.to_dict()
        bm.id = '0987654321'
        updated_dict = bm.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''

        dt = datetime.now()
        bm = BaseModel()
        bm.id = '1234567890'
        bm.created_at = dt
        bm.updated_at = dt
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(result['created_at'], iso_format))
        self.assertTrue(datetime.strptime(result['updated_at'], iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        bm = BaseModel()
        bm.id = '1234567890'
        bm.created_at = dt
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['id'], '1234567890')
        self.assertEqual(bm_dict['created_at'], dt)
        self.assertNotIn('mass', bm_dict)


if __name__ == "__main__":
    unittest.main()
