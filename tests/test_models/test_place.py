#!/usr/bin/python3
'''Defines the unittests for the child class - Place.'''

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace_init(unittest.TestCase):
    '''Unittests for the __init__ method of the Place class.'''

    def test_no_args(self):
        '''Test create an instance with no arguments.'''
        self.assertEqual(type(Place()), Place)

    def test_None_args(self):
        '''Test __init__method with None as an argument.'''
        a = Place(None)
        self.assertNotIn(None, a.__dict__.values())

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(Place().id), str)

    def test_unique_ids(self):
        '''Test that two instances of Place have unique ids.'''
        i1 = Place()
        i2 = Place()
        self.assertNotEqual(i1.id, i2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(Place().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = Place()
        sleep(1)
        i2 = Place()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(Place().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = Place()
        sleep(1)
        i2 = Place()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_city_id_is_public_str(self):
        '''Test that ``city_id`` is a string - public class attribute.'''
        self.assertEqual(type(Place().city_id), str)

    def test_user_id_is_public_str(self):
        '''Test that ``user_id`` is a string - public class attribute.'''
        self.assertEqual(type(Place().user_id), str)

    def test_name_is_public_str(self):
        '''Test that ``name`` is a string - public class attribute.'''
        self.assertEqual(type(Place().name), str)

    def test_description_is_public_str(self):
        '''Test that ``description`` is a string - public class attribute.'''
        self.assertEqual(type(Place().description), str)

    def test_number_rooms_is_public_int(self):
        '''Test that ``numer_rooms`` is an integer - public class attribute.'''
        self.assertEqual(type(Place().number_rooms), int)

    def test_number_bathrooms_is_public_int(self):
        '''Test that ``number_bathrooms`` is an integer class attribute.'''
        self.assertEqual(type(Place().number_bathrooms), int)

    def test_max_guest_is_public_int(self):
        '''Test that ``max_guest`` is an integer - public class attribute.'''
        self.assertEqual(type(Place().max_guest), int)

    def testlatitude_is_public_float(self):
        '''Test that ``latitude`` is a float - public class attribute.'''
        self.assertEqual(type(Place().latitude), float)

    def test_longitude_is_public_str(self):
        '''Test that ``longitude`` is a float - public class attribute.'''
        self.assertEqual(type(Place().longitude), float)

    def test_place_ids_is_public_list(self):
        '''Test that ``amenity_ids`` is a list - public class attribute.'''
        self.assertEqual(type(Place().amenity_ids), list)

    def test_init_with_kwargs(self):
        '''Create an instance of Place with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        a = Place(id='123', created_at=dt_isoformat,
                  updated_at=dt_isoformat)
        self.assertEqual(a.id, '123')
        self.assertEqual(a.created_at, dt)
        self.assertEqual(a.updated_at, dt)

    def test_datetime_attributes(self):
        '''Test that the created_at and updated_at are datetime attributes
                        when init with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        a = Place(id='123', created_at=dt_isoformat,
                  updated_at=dt_isoformat)
        self.assertEqual(type(a.created_at), datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_init_excludes_class_attributes(self):
        '''Tests that '__class__' key from kwargs
            is not added as an attribute.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        a = Place(id='123', created_at=dt_isoformat,
                  updated_at=dt_isoformat, __class__='Place')
        self.assertNotEqual(a.__class__, 'Place')

    def test_init_with_None_kwargs(self):
        '''Test __init__ methods with kwargs whose values are None.'''
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        '''Create an instance of Place with args and kwargs arguments.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        a = Place('1234', id='123', created_at=dt_isoformat,
                  updated_at=dt_isoformat)
        self.assertEqual(a.id, '123')
        self.assertEqual(a.created_at, dt)
        self.assertEqual(a.updated_at, dt)
        self.assertNotIn('1234', a.__dict__.values())


class TestPlace_str(unittest.TestCase):
    '''Unittests for the __str__ method of the Place class.'''

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        a = Place()
        a.id = '1234567890'
        a.created_at = dt
        a.updated_at = dt
        expected_str = '[Place] (1234567890) ' + str(a.__dict__)
        output_str = a.__str__()
        self.assertEqual(expected_str, output_str)


class TestPlace_save(unittest.TestCase):
    '''Unittests for the __save__ method of the Place class.'''

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
        a = Place()
        initial_updated_at = a.updated_at
        sleep(1)
        a.save()
        self.assertNotEqual(initial_updated_at, a.updated_at)
        self.assertLess(initial_updated_at, a.updated_at)

    def test_save_with_arg(self):
        '''Test calling the save method with an argument.'''
        a = Place()
        with self.assertRaises(TypeError):
            a.save('an_argument')

    def test_save_with_None_arg(self):
        '''Test calling the save method with None argument.'''
        a = Place()
        with self.assertRaises(TypeError):
            a.save(None)

    def test_save_updates_file(self):
        '''Test that the save method updates the JSON file with object.'''
        a = Place()
        a.save()
        id = 'Place.' + a.id
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertIn(id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the Place class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        a = Place()
        self.assertEqual(type(a.to_dict()), dict)

    def test_to_dict_contains_all_keys(self):
        '''Test to_dict returns a dictionary with all the expected keys.'''
        a = Place()
        a_dict = a.to_dict()
        self.assertIn("id", a.to_dict())
        self.assertIn("created_at", a_dict)
        self.assertIn("updated_at", a_dict)
        self.assertIn("__class__", a_dict)
        self.assertEqual(a_dict['__class__'], 'Place')

    def test_to_dict_includes_extra_attributes(self):
        '''Test that the to_dict method includes any added attributes.'''
        a = Place()
        a.name = 'Aishah'
        a.age = 17
        a_dict = a.to_dict()
        self.assertIn('name', a_dict)
        self.assertEqual(a_dict['name'], 'Aishah')
        self.assertIn('age', a_dict)
        self.assertEqual(a_dict['age'], 17)

    def test_to_dict_correct_output(self):
        '''Test that to_dict method returns the correct dictionary.'''
        dt = datetime.now()
        a = Place()
        a.id = '1234567890'
        a.created_at = a.updated_at = dt
        expected_dict = {
                'id': '1234567890',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                '__class__': 'Place'
        }
        self.assertDictEqual(a.to_dict(), expected_dict)

    def test_datetime_attribute_value_type(self):
        '''Tests if created_at and updated_at values  are strings.'''
        a = Place()
        a_dict = a.to_dict()
        self.assertEqual(type(a_dict['created_at']), str)
        self.assertEqual(type(a_dict['updated_at']), str)

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        a = Place()
        a.id = '1234567890'
        initial_dict = a.to_dict()
        a.id = '0987654321'
        updated_dict = a.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''
        dt = datetime.now()
        a = Place()
        a.id = '1234567890'
        a.created_at = dt
        a.updated_at = dt
        a_dict = a.to_dict()
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(a_dict['created_at'], iso_format))
        self.assertTrue(datetime.strptime(a_dict['updated_at'], iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        a = Place()
        a.id = '1234567890'
        a.created_at = dt
        a_dict = a.to_dict()
        self.assertEqual(a_dict['id'], '1234567890')
        self.assertEqual(a_dict['created_at'], dt.isoformat())
        self.assertNotIn('mass', a_dict)

    def test_to_dict_not__dict__(self):
        '''Test that to_dict method is not the same as the special __dict__.'''
        a = Place()
        self.assertNotEqual(a.to_dict(), a.__dict__)

    def test_to_dict_with_arg(self):
        '''Test the to_dict method with an argument.'''
        a = Place()
        with self.assertRaises(TypeError):
            a.to_dict('an_argument')

    def test_to_dict_with_None_arg(self):
        ''''Test the to_dict method with None argument.'''
        a = Place()
        with self.assertRaises(TypeError):
            a.to_dict(None)


if __name__ == "__main__":
    unittest.main()
