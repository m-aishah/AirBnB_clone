#!/usr/bin/python3
'''Defines the unittests for the child class - State.'''

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    '''Unittests for the State class.'''

    def test_init_no_args(self):
        '''Create an instance of State with no aruments.'''
        self.assertEqual(type(State()), State)

    def test_instance_stored_in_objects(self):
        '''Test new instance of State class is stored in storage's objects.'''
        self.assertIn(State(), models.storage.all().values())

    def test_None_args(self):
        '''Test __init__method with None as an argument.'''
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(State().id), str)

    def test_unique_ids(self):
        '''Test that two instances of State have unique ids.'''
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(State().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = State()
        sleep(1)
        i2 = State()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(State().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = State()
        sleep(1)
        i2 = State()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_name_public_str(self):
        '''Test that ``name`` is a public class attribute.'''
        self.assertEqual(type(State().name), str)

    def test_init_with_kwargs(self):
        '''Create an instance of State with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        state = State(id='123', created_at=dt_isoformat,
                      updated_at=dt_isoformat)
        self.assertEqual(state.id, '123')
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_datetime_attributes(self):
        '''Test that the created_at and updated_at are datetime attributes
                        when init with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        state = State(id='123', created_at=dt_isoformat,
                      updated_at=dt_isoformat)
        self.assertEqual(type(state.created_at), datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_init_excludes_class_attributes(self):
        '''Tests that '__class__' key from kwargs
            is not added as an attribute.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        state = State(id='123', created_at=dt_isoformat,
                      updated_at=dt_isoformat, __class__='State')
        self.assertNotEqual(state.__class__, 'State')

    def test_init_with_None_kwargs(self):
        '''Test __init__ methods with kwargs whose values are None.'''
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        '''Create an instance of State with args and kwargs arguments.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        state = State('1234', id='123', created_at=dt_isoformat,
                      updated_at=dt_isoformat)
        self.assertEqual(state.id, '123')
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)
        self.assertNotIn('1234', state.__dict__.values())


class TestState_str(unittest.TestCase):
    '''Unittests for the __str__ method of the State class.'''

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        state = State()
        state.id = '1234567890'
        state.created_at = dt
        state.updated_at = dt
        expected_str = '[State] (1234567890) ' + str(state.__dict__)
        output_str = state.__str__()
        self.assertEqual(expected_str, output_str)


class TestState_save(unittest.TestCase):
    '''Unittests for the __save__ method of the State class.'''

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
        state = State()
        initial_updated_at = state.updated_at
        sleep(1)
        state.save()
        self.assertNotEqual(initial_updated_at, state.updated_at)
        self.assertLess(initial_updated_at, state.updated_at)

    def test_save_with_arg(self):
        '''Test calling the save method with an argument.'''
        state = State()
        with self.assertRaises(TypeError):
            state.save('an_argument')

    def test_save_with_None_arg(self):
        '''Test calling the save method with None argument.'''
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        '''Test that the save method updates the JSON file with object.'''
        state = State()
        state.save()
        id = 'State.' + state.id
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertIn(id, f.read())


class TestState_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the State class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        state = State()
        self.assertEqual(type(state.to_dict()), dict)

    def test_to_dict_contains_all_keys(self):
        '''Test to_dict returns a dictionary with all the expected keys.'''
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_to_dict_includes_extra_attributes(self):
        '''Test that the to_dict method includes any added attributes.'''
        state = State()
        state.name = 'Aishah'
        state.age = 17
        state_dict = state.to_dict()
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], 'Aishah')
        self.assertIn('age', state_dict)
        self.assertEqual(state_dict['age'], 17)

    def test_to_dict_correct_output(self):
        '''Test that to_dict method returns the correct dictionary.'''
        dt = datetime.now()
        state = State()
        state.id = '1234567890'
        state.created_at = state.updated_at = dt
        expected_dict = {
                'id': '1234567890',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                '__class__': 'State'
        }
        self.assertDictEqual(state.to_dict(), expected_dict)

    def test_datetime_attribute_value_type(self):
        '''Tests if created_at and updated_at values  are strings.'''
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        state = State()
        state.id = '1234567890'
        initial_dict = state.to_dict()
        state.id = '0987654321'
        updated_dict = state.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''
        dt = datetime.now()
        state = State()
        state.id = '1234567890'
        state.created_at = dt
        state.updated_at = dt
        state_dict = state.to_dict()
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(state_dict['created_at'],
                        iso_format))
        self.assertTrue(datetime.strptime(state_dict['updated_at'],
                        iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        state = State()
        state.id = '1234567890'
        state.created_at = dt
        state_dict = state.to_dict()
        self.assertEqual(state_dict['id'], '1234567890')
        self.assertEqual(state_dict['created_at'], dt.isoformat())
        self.assertNotIn('mass', state_dict)

    def test_to_dict_not__dict__(self):
        '''Test that to_dict method is not the same as the special __dict__.'''
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg(self):
        '''Test the to_dict method with an argument.'''
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict('an_argument')

    def test_to_dict_with_None_arg(self):
        ''''Test the to_dict method with None argument.'''
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == '__main__':
    unittest.main()
