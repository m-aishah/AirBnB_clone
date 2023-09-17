#!/usr/bin/python3
'''Defines unittests for the child class - City.'''

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity_init(unittest.TestCase):
    '''Unittests for the __init__ method of the City class.'''

    def test_no_args(self):
        '''Test create an instance with no arguments.'''
        self.assertEqual(type(City()), City)

    def test_None_args(self):
        '''Test __init__method with None as an argument.'''
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(City().id), str)

    def test_unique_ids(self):
        '''Test that two instances of City have unique ids.'''
        i1 = City()
        i2 = City()
        self.assertNotEqual(i1.id, i2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(City().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = City()
        sleep(1)
        i2 = City()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(City().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = City()
        sleep(1)
        i2 = City()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_state_id_is_public_str(self):
        '''Test that state_id is a string - public class attribute.'''
        self.assertEqual(type(City().state_id), str)

    def test_name_is_public_str(self):
        '''Test that name is a string - public class attribute.'''
        self.assertEqual(type(City().name), str)

    def test_init_with_kwargs(self):
        '''Create an instance of City with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        city = City(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat)
        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_datetime_attributes(self):
        '''Test that the created_at and updated_at are datetime attributes
                        when init with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        city = City(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat)
        self.assertEqual(type(city.created_at), datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_init_excludes_class_attributes(self):
        '''Tests that '__class__' key from kwargs
            is not added as an attribute.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        city = City(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat, __class__='City')
        self.assertNotEqual(city.__class__, 'City')

    def test_init_with_None_kwargs(self):
        '''Test __init__ methods with kwargs whose values are None.'''
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        '''Create an instance of City with args and kwargs arguments.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        city = City('1234', id='123', created_at=dt_isoformat,
                    updated_at=dt_isoformat)
        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)
        self.assertNotIn('1234', city.__dict__.values())


class TestCity_str(unittest.TestCase):
    '''Unittests for the __str__ method of the City class.'''

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        city = City()
        city.id = '1234567890'
        city.created_at = dt
        city.updated_at = dt
        expected_str = '[City] (1234567890) ' + str(city.__dict__)
        output_str = city.__str__()
        self.assertEqual(expected_str, output_str)


class TestCity_save(unittest.TestCase):
    '''Unittests for the __save__ method of the City class.'''

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        '''Test if save updates the updated_at time'''
        city = City()
        initial_updated_at = city.updated_at
        sleep(1)
        city.save()
        self.assertNotEqual(initial_updated_at, city.updated_at)
        self.assertLess(initial_updated_at, city.updated_at)

    def test_save_with_arg(self):
        '''Test calling the save method with an argument.'''
        city = City()
        with self.assertRaises(TypeError):
            city.save('an_argument')

    def test_save_with_None_arg(self):
        '''Test calling the save method with None argument.'''
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        '''Test that the save method updates the JSON file with object.'''
        city = City()
        city.save()
        id = 'City.' + city.id
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertIn(id, f.read())


class TestCity_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the City class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        city = City()
        self.assertEqual(type(city.to_dict()), dict)

    def test_to_dict_contains_all_keys(self):
        '''Test to_dict returns a dictionary with all the expected keys.'''
        city = City()
        city_dict = city.to_dict()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_to_dict_includes_extra_attributes(self):
        '''Test that the to_dict method includes any added attributes.'''
        city = City()
        city.name = 'Aishah'
        city.age = 17
        city_dict = city.to_dict()
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['name'], 'Aishah')
        self.assertIn('age', city_dict)
        self.assertEqual(city_dict['age'], 17)

    def test_to_dict_correct_output(self):
        '''Test that to_dict method returns the correct dictionary.'''
        dt = datetime.now()
        city = City()
        city.id = '1234567890'
        city.created_at = city.updated_at = dt
        expected_dict = {
                'id': '1234567890',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                '__class__': 'City'
        }
        self.assertDictEqual(city.to_dict(), expected_dict)

    def test_datetime_attribute_value_type(self):
        '''Tests if created_at and updated_at values  are strings.'''
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        city = City()
        city.id = '1234567890'
        initial_dict = city.to_dict()
        city.id = '0987654321'
        updated_dict = city.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''
        dt = datetime.now()
        city = City()
        city.id = '1234567890'
        city.created_at = dt
        city.updated_at = dt
        city_dict = city.to_dict()
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(city_dict['created_at'], iso_format))
        self.assertTrue(datetime.strptime(city_dict['updated_at'], iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        city = City()
        city.id = '1234567890'
        city.created_at = dt
        city_dict = city.to_dict()
        self.assertEqual(city_dict['id'], '1234567890')
        self.assertEqual(city_dict['created_at'], dt.isoformat())
        self.assertNotIn('mass', city_dict)

    def test_to_dict_not__dict__(self):
        '''Test that to_dict method is not the same as the special __dict__.'''
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        '''Test the to_dict method with an argument.'''
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict('an_argument')

    def test_to_dict_with_None_arg(self):
        ''''Test the to_dict method with None argument.'''
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
