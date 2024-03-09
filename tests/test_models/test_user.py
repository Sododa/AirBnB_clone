#!/usr/bin/python3
"""writes a class TestUser for User module. """
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """writes tests for User Class"""

    @classmethod
    def setUp(cls):
        """sets up for each test case.
        """
        cls.user1 = User()
        cls.user1.name = "Wendy"

    @classmethod
    def tearDown(cls):
        """tears up after each test.
        """
        del cls.user1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.user1)), result)

    def test_inheritance(self):
        """Test inheritance instace of BaseModel.
        """
        self.assertIsInstance(self.user1, User)
        self.assertEqual(type(self.user1), User)
        self.assertEqual(issubclass(self.user1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type.
        """
        self.assertIsInstance(self.user1.id, str)
        self.assertEqual(type(self.user1.id), str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)

    def test_save(self):
        """Test if save works correctly after update.
        """
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_functions(self):
        """Test functions for User module is documented.
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Test has expected attributes exist.
        """
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))

    def test_to_dict(self):
        """Test for to_dict method is works correctly.
        """
        my_model_json = self.user1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.user1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.user1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.user1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.user1.id)

    def test_unique_id(self):
        """Test for a unique ID.
        """
        user2 = self.user1.__class__()
        user3 = self.user1.__class__()
        user4 = self.user1.__class__()
        self.assertNotEqual(self.user1.id, user2.id)
        self.assertNotEqual(self.user1.id, user3.id)
        self.assertNotEqual(self.user1.id, user4.id)


if __name__ == '__main__':
    unittest.main()
