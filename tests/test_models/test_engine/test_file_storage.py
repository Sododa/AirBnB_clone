#!/usr/bin/python3
""" writes a class TestFileStorage for FileStorage module. """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """writes tests for FileStorage Class"""

    @classmethod
    def setUp(cls):
        """setup for each test case.
        """
        cls.base_model1 = BaseModel()
        cls.file_storage1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """tears up after each test.
        """
        del cls.base_model1
        del cls.file_storage1

    def test_class_exists(self):
        """Test if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.file_storage1)), result)

    def test_types(self):
        """Test  for attributes type is correct.
        """
        self.assertIsInstance(self.file_storage1, FileStorage)
        self.assertEqual(type(self.file_storage1), FileStorage)

    def test_functions(self):
        """Test if Function documented.
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """Test if save method is working correctly.
        """
        self.file_storage1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Tests for reload method works correctly.
        """
        self.base_model1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
