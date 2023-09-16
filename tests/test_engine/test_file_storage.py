#!/usr/bin/env python3
'''Defines the unittests for models/engine/file_storage.py.'''

import os
import json
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_init(unittest.TestCase):
    '''Unittests for the __init__ method of the FileStorage class.'''

    def test_FileStorage_no_args(self):
        ''''Test that the FileStirage initializes with no arguments.'''
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        '''Test raises error when initialised with an argument.'''
        with self.assertRaises(TypeError):
            FileStorage('an_argument')

    def test_FileStorage_None_arg(self):
        ''''Test that error is raised when initialised with None argument.'''
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path(self):
        '''Test that file_path is a string - private class atribute.'''
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        ''''Test that the objects is a dict - private class attribute.'''
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_initializes(self):
        '''Test storage initialized as an instance of the FileStorage class.'''
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_all(unittest.TestCase):
    '''Unittests for the public class method - all().'''

    @classmethod
    def SetUp(self):
        # If file.json exists rename it as tmp before carrying out the tests.
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def TearDown(self):
        # If after the tests, file.json exists, delete it.
        try:
            os.remove("file.json")
        except IOError:
            pass

        # If a file.json was renamed tmp during SetUp,
        # rename it back to its original.
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        '''Test that all method returns a dictionary.'''
        self.assertEqual(type(FileStorage().all()), dict)

    def test_all_with_arg(self):
        '''Test the all method with an argument.'''
        with self.assertRaises(TypeError):
            FileStorage().all('an_argument')

    def test_all_with_None_arg(self):
        '''Test the all method with None argument.'''
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_correct_output(self):
        '''Test that the all method returns the correct dictionary.'''
        bm = BaseModel()
        self.assertIn('BaseModel.' + bm.id, models.storage.all().keys())


class TestFileStorage_new(unittest.TestCase):
    '''Unittests for the public instance method - new().'''

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
        FileStorage._FileStorage__objects = {}

    def test_new_no_args(self):
        '''Test the new method with no arguments.'''
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_None_arg(self):
        '''Test the new method with None argument.'''
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_string_attribute(self):
        ''''Test the new method with a string argument.'''
        with self.assertRaises(AttributeError):
            models.storage.new('a_string')

    def test_dict_attribute(self):
        '''Test the new method with a dict argument'''
        with self.assertRaises(AttributeError):
            models.storage.new({'id': '1234', 'created_at': datetime.now(),
                                'updated_at': datetime.now()})

    def test_new(self):
        '''Test the new method.'''
        bm = BaseModel()
        models.storage.new(bm)
        objects = models.storage.all()
        self.assertIn('BaseModel.' + bm.id, objects.keys())
        self.assertIn(bm, objects.values())


class TestFileStorage_save(unittest.TestCase):
    '''Unittests for the public instance method - save().'''

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
        FileStorage._FileStorage__objects = {}

    def test_save_one_object(self):
        '''Test te save method with two objects.'''
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertIn(json.dumps(bm.to_dict()), file_content)
            self.assertIn("BaseModel." + bm.id, file_content)

    def test_save_two_objects(self):
        '''Test the save method with two objects.'''
        bm1 = BaseModel()
        bm2 = BaseModel()
        models.storage.save()
        with open('file.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertIn(json.dumps(bm1.to_dict()), file_content)
            self.assertIn('BaseModel.' + bm1.id, file_content)
            self.assertIn(json.dumps(bm2.to_dict()), file_content)
            self.assertIn('BaseModel.' + bm2.id, file_content)

    def test_save_with_arg(self):
        '''Test the save method with an argument.'''
        with self.assertRaises(TypeError):
            models.storage.save('an_argument')

    def test_save_with_None_args(self):
        '''Test the save method with None argument.'''
        with self.assertRaises(TypeError):
            models.storage.save(None)


class TestFileStorage_reload(unittest.TestCase):
    '''Unittests for the public instance method - reload().'''

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
        FileStorage._FileStorage__objects = {}

    def test_reload(self):
        '''Test the reload method.'''
        bm = BaseModel()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        objects = models.storage.all()
        self.assertIn('BaseModel.' + bm.id, objects)

    def test_reload_one_arg(self):
        '''Test the reload method with one argument.'''
        bm = BaseModel()
        models.storage.save()
        with self.assertRaises(TypeError):
            models.storage.reload('an_argument')

    def test_reload_None_arg(self):
        '''Test the reload method with None argument.'''
        bm = BaseModel()
        models.storage.save()
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_no_json_file(self):
        '''Test the reload method when the json file does not exist.'''
        self.assertIsNone(models.storage.reload())


if __name__ == '__main__':
    unittest.main()
