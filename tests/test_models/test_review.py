#!/usr/bin/python3
'''Defines unittests for the child class - Review.'''

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview_init(unittest.TestCase):
    '''Unittests for the __init__ method of the Review class.'''

    def test_no_args(self):
        '''Test create an instance with no arguments.'''
        self.assertEqual(type(Review()), Review)

    def test_None_args(self):
        '''Test __init__method with None as an argument.'''
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_id_is_str(self):
        '''Test that ``id`` is a public string attribute.'''
        self.assertEqual(type(Review().id), str)

    def test_unique_ids(self):
        '''Test that two instances of Review have unique ids.'''
        i1 = Review()
        i2 = Review()
        self.assertNotEqual(i1.id, i2.id)

    def test_created_at_is_datetime(self):
        '''Test that ``created_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(Review().created_at), datetime)

    def test_created_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``created_at``.'''
        i1 = Review()
        sleep(1)
        i2 = Review()
        self.assertNotEqual(i1.created_at, i2.created_at)
        self.assertLess(i1.created_at, i2.created_at)

    def test_updated_at_is_datetime(self):
        '''Test that ``updated_at`` is a publis attribute of type datettime.'''
        self.assertEqual(type(Review().updated_at), datetime)

    def test_updated_at_right_time(self):
        '''Test that two models created at separate times,
                            have different ``updated_at``.'''
        i1 = Review()
        sleep(1)
        i2 = Review()
        self.assertNotEqual(i1.updated_at, i2.updated_at)
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_place_id_is_public_str(self):
        '''Test that ``place_id`` is a string - public class attribute.'''
        self.assertEqual(type(Review().place_id), str)

    def test_user_id_is_public_str(self):
        '''Test that ``user_id`` is a string - public class attribute.'''
        self.assertEqual(type(Review().user_id), str)

    def test_text_is_public_str(self):
        '''Test that ``text`` is a string - public class attribute.'''
        self.assertEqual(type(Review().text), str)

    def test_init_with_kwargs(self):
        '''Create an instance of Review with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        review = Review(id='123', created_at=dt_isoformat,
                        updated_at=dt_isoformat)
        self.assertEqual(review.id, '123')
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_datetime_attributes(self):
        '''Test that the created_at and updated_at are datetime attributes
                        when init with **kwargs.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        review = Review(id='123', created_at=dt_isoformat,
                        updated_at=dt_isoformat)
        self.assertEqual(type(review.created_at), datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_init_excludes_class_attributes(self):
        '''Tests that '__class__' key from kwargs
            is not added as an attribute.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        review = Review(id='123', created_at=dt_isoformat,
                        updated_at=dt_isoformat, __class__='Review')
        self.assertNotEqual(review.__class__, 'Review')

    def test_init_with_None_kwargs(self):
        '''Test __init__ methods with kwargs whose values are None.'''
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        '''Create an instance of Review with args and kwargs arguments.'''
        dt = datetime.now()
        dt_isoformat = dt.isoformat()
        review = Review('1234', id='123', created_at=dt_isoformat,
                        updated_at=dt_isoformat)
        self.assertEqual(review.id, '123')
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)
        self.assertNotIn('1234', review.__dict__.values())


class TestReview_str(unittest.TestCase):
    '''Unittests for the __str__ method of the Review class.'''

    def test_str_method(self):
        '''Test the __str__ public string method.'''
        dt = datetime.now()
        review = Review()
        review.id = '1234567890'
        review.created_at = dt
        review.updated_at = dt
        expected_str = '[Review] (1234567890) ' + str(review.__dict__)
        output_str = review.__str__()
        self.assertEqual(expected_str, output_str)


class TestReview_save(unittest.TestCase):
    '''Unittests for the __save__ method of the Review class.'''

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
        review = Review()
        initial_updated_at = review.updated_at
        sleep(1)
        review.save()
        self.assertNotEqual(initial_updated_at, review.updated_at)
        self.assertLess(initial_updated_at, review.updated_at)

    def test_save_with_arg(self):
        '''Test calling the save method with an argument.'''
        review = Review()
        with self.assertRaises(TypeError):
            review.save('an_argument')

    def test_save_with_None_arg(self):
        '''Test calling the save method with None argument.'''
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        '''Test that the save method updates the JSON file with object.'''
        review = Review()
        review.save()
        id = 'Review.' + review.id
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertIn(id, f.read())


class TestReview_to_dict(unittest.TestCase):
    '''Unittests for the __to_dict__ method of the Review class.'''

    def test_to_dict(self):
        '''Tests if to_dict returns a dictionary'''
        review = Review()
        self.assertEqual(type(review.to_dict()), dict)

    def test_to_dict_contains_all_keys(self):
        '''Test to_dict returns a dictionary with all the expected keys.'''
        review = Review()
        review_dict = review.to_dict()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_to_dict_includes_extra_attributes(self):
        '''Test that the to_dict method includes any added attributes.'''
        review = Review()
        review.name = 'Aishah'
        review.age = 17
        review_dict = review.to_dict()
        self.assertIn('name', review_dict)
        self.assertEqual(review_dict['name'], 'Aishah')
        self.assertIn('age', review_dict)
        self.assertEqual(review_dict['age'], 17)

    def test_to_dict_correct_output(self):
        '''Test that to_dict method returns the correct dictionary.'''
        dt = datetime.now()
        review = Review()
        review.id = '1234567890'
        review.created_at = review.updated_at = dt
        expected_dict = {
                'id': '1234567890',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                '__class__': 'Review'
        }
        self.assertDictEqual(review.to_dict(), expected_dict)

    def test_datetime_attribute_value_type(self):
        '''Tests if created_at and updated_at values  are strings.'''
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_to_dict_updates(self):
        '''Tests that to_dict reflects updated value'''
        review = Review()
        review.id = '1234567890'
        initial_dict = review.to_dict()
        review.id = '0987654321'
        updated_dict = review.to_dict()
        self.assertNotEqual(initial_dict['id'], updated_dict['id'])
        self.assertEqual(updated_dict['id'], "0987654321")

    def test_to_dict_ISO(self):
        '''Tests that created_at and updated_at are in ISO format'''
        dt = datetime.now()
        review = Review()
        review.id = '1234567890'
        review.created_at = dt
        review.updated_at = dt
        review_dict = review.to_dict()
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertTrue(datetime.strptime(review_dict['created_at'],
                        iso_format))
        self.assertTrue(datetime.strptime(review_dict['updated_at'],
                        iso_format))

    def test_only_instance_attributes(self):
        '''Tests that to_dict returns only instance attributes set'''
        dt = datetime.now()
        review = Review()
        review.id = '1234567890'
        review.created_at = dt
        review_dict = review.to_dict()
        self.assertEqual(review_dict['id'], '1234567890')
        self.assertEqual(review_dict['created_at'], dt.isoformat())
        self.assertNotIn('mass', review_dict)

    def test_to_dict_not__dict__(self):
        '''Test that to_dict method is not the same as the special __dict__.'''
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_to_dict_with_arg(self):
        '''Test the to_dict method with an argument.'''
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict('an_argument')

    def test_to_dict_with_None_arg(self):
        ''''Test the to_dict method with None argument.'''
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
