#!/usr/bin/python3
""" writes a class TestAmenity for Amenity module. """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime


class TestAmenity(unittest.TestCase):
    """writes tests an Amenity Class"""

    @classmethod
    def setUp(cls):
        """set up define test case.
        """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Parking"

    @classmethod
    def tearDown(cls):
        """tear down up after each test.
        """
        del cls.amenity1

    def test_class_exists(self):
        """used to tset if the class exists.
        """
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity1)), result)

    def test_inheritance(self):
        """Test for Amenity is a subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.amenity1, Amenity)
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertEqual(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_types(self):
        """Test for a correct attributes type is correct.
        """
        self.assertIsInstance(self.amenity1.name, str)
        self.assertEqual(type(self.amenity1.name), str)
        self.assertIsInstance(self.amenity1.id, str)
        self.assertEqual(type(self.amenity1.id), str)
        self.assertIsInstance(self.amenity1.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity1.updated_at, datetime.datetime)

    def test_save(self):
        """Test that the  save method is working correctly after update.
        """
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_functions(self):
        """Test that the  Amenity moudule is documented.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """Test that the  expected attributes exist.
        """
        self.assertTrue(hasattr(self.amenity1, 'name'))
        self.assertTrue(hasattr(self.amenity1, 'id'))
        self.assertTrue(hasattr(self.amenity1, 'created_at'))
        self.assertTrue(hasattr(self.amenity1, 'updated_at'))

    def test_to_dict(self):
        """Test that if  to_dict method is working correctly.
        """
        my_model_json = self.amenity1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.amenity1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.amenity1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.amenity1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.amenity1.id)

    def test_unique_id(self):
        """Test if each instance is created with a unique ID.
        """
        amenity2 = self.amenity1.__class__()
        amenity3 = self.amenity1.__class__()
        amenity4 = self.amenity1.__class__()
        self.assertNotEqual(self.amenity1.id, amenity2.id)
        self.assertNotEqual(self.amenity1.id, amenity3.id)
        self.assertNotEqual(self.amenity1.id, amenity4.id)


if __name__ == '__main__':
    unittest.main()
