#!/usr/bin/python3
"""writes a class TestBaseModel for BaseModel module. """
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """writes tests for Amenity Class"""

    @classmethod
    def setUp(cls):
        """it sets up for each test case.
        """
        cls.BaseModel1 = BaseModel()
        cls.BaseModel1.name = "Samsung"
        cls.BaseModel1.my_number = 89

    @classmethod
    def tearDown(cls):
        """tears down up after each test.
        """
        del cls.BaseModel1

    def test_class_exists(self):
        """Tests that the class exists.
        """
        result = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.BaseModel1)), result)

    def testBaseModel1(self):
        """Test attributes if BaseModel instance.
        """
        self.BaseModel1.save()
        my_model_json = self.BaseModel1.to_dict()

        self.assertEqual(self.BaseModel1.name, my_model_json['name'])
        self.assertEqual(self.BaseModel1.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.BaseModel1.id, my_model_json['id'])

    def test_types(self):
        """Test for correct attributes type
        """
        self.assertIsInstance(self.BaseModel1.name, str)
        self.assertEqual(type(self.BaseModel1.name), str)
        self.assertIsInstance(self.BaseModel1.id, str)
        self.assertEqual(type(self.BaseModel1.id), str)
        self.assertIsInstance(self.BaseModel1.created_at, datetime.datetime)
        self.assertIsInstance(self.BaseModel1.updated_at, datetime.datetime)

    def test_save(self):
        """Test save method works correctly after update.
        """
        self.BaseModel1.save()
        self.assertNotEqual(self.BaseModel1.created_at,
                            self.BaseModel1.updated_at)

    def test_functions(self):
        """Test if functions is documented.
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_attributes(self):
        """Test has attributes exist.
        """
        self.assertTrue(hasattr(self.BaseModel1, 'name'))
        self.assertTrue(hasattr(self.BaseModel1, 'id'))
        self.assertTrue(hasattr(self.BaseModel1, 'created_at'))
        self.assertTrue(hasattr(self.BaseModel1, 'updated_at'))

    def test_set_attributes(self):
        """Test set attributes that BaseModel.
        """
        self.assertEqual(self.BaseModel1.name, "Samsung")
        self.assertEqual(self.BaseModel1.my_number, 89)

    def test_to_dict(self):
        """Test if to_dict method works correctly.
        """
        my_model_json = self.BaseModel1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.BaseModel1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.BaseModel1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.BaseModel1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.BaseModel1.id)

    def test_unique_id(self):
        """Test that each instance is created with a unique ID.
        """
        basemodel2 = self.BaseModel1.__class__()
        basemodel3 = self.BaseModel1.__class__()
        basemodel4 = self.BaseModel1.__class__()
        self.assertNotEqual(self.BaseModel1.id, basemodel2.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel3.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel4.id)


if __name__ == '__main__':
    unittest.main()
