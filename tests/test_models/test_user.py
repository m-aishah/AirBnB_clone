#!/usr/bin/python3
''' Defines unittests for child class - User.'''

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser_init(unittest.TestCase):
    '''Unittests for the __init__ method of the User class.'''

    def test_no_args(self):
        '''Test create an instance with no arguments.'''
        self.assertEqual(type(User()), User)

    def test_None_args(self):
        '''Test __init__method with None as an argument.'''
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(User().id), str)

    def test_unique_ids(self):
        '''Test that two instances of User have unique ids.'''
        i1 = User()
        i2 = User()
        self.assertNotEqual(i1.id, i2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a public attribute of type datettime.'''
        self.assertEqual(type(User().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = User()
        sleep(1)
        i2 = User()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(User().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = User()
        sleep(1)
        i2 = User()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_email_is_public_str(self):
        '''Test that email is a string - public class attribute.'''
        self.assertEqual(type(User().email), str)

    def test_password_is_public_str(self):
        '''Test that paswword is a string - public class attribute.'''
        self.assertEqual(type(User().password), str)

    def test_first_name_is_public_str(self):
        '''Test that first_name is a string - public class attribute.'''
        self.assertEqual(type(User().first_name), str)

    def test_last_name_is_public_str(self):
        '''Test that last_name is a string - public class attribute.'''
        self.assertEqual(type(User().last_name), str)

    def test_init_with_kwargs(self):
        '''Create an instance of User with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        user = User(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_datetime_attributes(self):
        '''Test that the created_at and updated_at are datetime attributes
                        when init with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        user = User(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat)
        self.assertEqual(type(user.created_at), datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_init_excludes_class_attributes(self):
        '''Tests that '__class__' key from kwargs
            is not added as an attribute.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        user = User(id='123', created_at=dt_isoformat,
                       updated_at=dt_isoformat, __class__='User')
        self.assertNotEqual(user.__class__, 'User')

    def test_init_with_None_kwargs(self):
        '''Test __init__ methods with kwargs whose values are None.'''
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        '''Create an instance of User with args and kwargs arguments.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        user = User('1234', id='123', created_at=dt_isoformat,
                    updated_at=dt_isoformat)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)
        self.assertNotIn('1234', user.__dict__.values())


class TestUser_str(unittest.TestCase):
    '''Unittests for the __str__ method of the User class.'''

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        user = User()
        user.id = '1234567890'
        user.created_at = dt
        user.updated_at = dt
        expected_str = '[User] (1234567890) ' + str(user.__dict__)
        output_str = user.__str__()
        self.assertEqual(expected_str, output_str)


class TestUser_save(unittest.TestCase):
    '''Unittests for the __save__ method of the User class.'''

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
        user = User()
        initial_updated_at = user.updated_at
        sleep(1)
        user.save()
        self.assertNotEqual(initial_updated_at, user.updated_at)
        self.assertLess(initial_updated_at, user.updated_at)

    def test_save_with_arg(self):
        '''Test calling the save method with an argument.'''
        user = User()
        with self.assertRaises(TypeError):
            user.save('an_argument')

    def test_save_with_None_arg(self):
        '''Test calling the save method with None argument.'''
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        '''Test that the save method updates the JSON file with object.'''
        user = User()
        user.save()
        id = 'User.' + user.id
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertIn(id, f.read())


class TestUser_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the User class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        user = User()
        self.assertEqual(type(user.to_dict()), dict)

    def test_to_dict_contains_all_keys(self):
        '''Test to_dict returns a dictionary with all the expected keys.'''
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_to_dict_includes_extra_attributes(self):
        '''Test that the to_dict method includes any added attributes.'''
        user = User()
        user.name = 'Aishah'
        user.age = 17
        user_dict = user.to_dict()
        self.assertIn('name', user_dict)
        self.assertEqual(user_dict['name'], 'Aishah')
        self.assertIn('age', user_dict)
        self.assertEqual(user_dict['age'], 17)

    def test_to_dict_correct_output(self):
        '''Test that to_dict method returns the correct dictionary.'''
        dt = datetime.now()
        user = User()
        user.id = '1234567890'
        user.created_at = user.updated_at = dt
        expected_dict = {
                'id': '1234567890',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                '__class__': 'User'
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_datetime_attribute_value_type(self):
        '''Tests if created_at and updated_at values  are strings.'''
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        user = User()
        user.id = '1234567890'
        initial_dict = user.to_dict()
        user.id = '0987654321'
        updated_dict = user.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''
        dt = datetime.now()
        user = User()
        user.id = '1234567890'
        user.created_at = dt
        user.updated_at = dt
        user_dict = user.to_dict()
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(user_dict['created_at'], iso_format))
        self.assertTrue(datetime.strptime(user_dict['updated_at'], iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        user = User()
        user.id = '1234567890'
        user.created_at = dt
        user_dict = user.to_dict()
        self.assertEqual(user_dict['id'], '1234567890')
        self.assertEqual(user_dict['created_at'], dt.isoformat())
        self.assertNotIn('mass', user_dict)

    def test_to_dict_not__dict__(self):
        '''Test that to_dict method is not the same as the special __dict__.'''
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        '''Test the to_dict method with an argument.'''
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict('an_argument')

    def test_to_dict_with_None_arg(self):
        ''''Test the to_dict method with None argument.'''
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
