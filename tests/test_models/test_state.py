#!/usr/bin/python3
""" writes a class TestState for State module. """
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """writes tests for State Class"""

    @classmethod
    def setUp(cls):
        """defines setup for each test case.
        """
        cls.state1 = State()
        cls.state1.name = "Nairobi"

    @classmethod
    def tearDown(cls):
        """tears up after each test.
        """
        del cls.state1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state1)), result)

    def test_inheritance(self):
        """Test inheritance of BaseModel.
        """
        self.assertIsInstance(self.state1, State)
        self.assertEqual(type(self.state1), State)
        self.assertEqual(issubclass(self.state1.__class__, BaseModel), True)

    def test_types(self):
        """Test for correct attributes.
        """
        self.assertIsInstance(self.state1.id, str)
        self.assertEqual(type(self.state1.id), str)
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)
        self.assertIsInstance(self.state1.name, str)

    def test_save(self):
        """Test for save method is works correctly after update.
        """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_functions(self):
        """Test if State module documented.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Test has attributes exist.
        """
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))
        self.assertTrue(hasattr(self.state1, 'name'))

    def test_to_dict(self):
        """Test to_dict method is works correctly.
        """
        my_model_json = self.state1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.state1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.state1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.state1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.state1.id)

    def test_unique_id(self):
        """Test for  instance is created with a unique ID.
        """
        state2 = self.state1.__class__()
        state3 = self.state1.__class__()
        state4 = self.state1.__class__()
        self.assertNotEqual(self.state1.id, state2.id)
        self.assertNotEqual(self.state1.id, state3.id)
        self.assertNotEqual(self.state1.id, state4.id)


if __name__ == '__main__':
    unittest.main()
