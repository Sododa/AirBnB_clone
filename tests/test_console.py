#!/usr/bin/python3
"""Defines unittests used for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Base class for test Console.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """tear FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_simple(self):
        """Tests simple commands.
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")


class TestBaseModel(unittest.TestCase):
    """ unit test for test base model commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """teardown  FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel self object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_basemodel(self):
        """Test all base model self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "brown"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cocelia"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ace"')
            self.assertEqual(b1.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(f'update BaseModel {b1.id} age 25')
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {b1.id} savings 35.89')
            self.assertIn("savings", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'update BaseModel {b1.id} age 10 color "brown"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object self.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestBaseModelDotNotation(unittest.TestCase):
    """Testing `Basemodel `commands using dot notation self.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """tears FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'BaseModel.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test count basemodel object count.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test all basemodel object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel self object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, name, "Ace")'))
            self.assertEqual(b1.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, age, 25)'))
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'BaseModel.update({b1.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_update_basemodel_dict(self):
        """Test update basemodel dictionary object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            cmmd = f'BaseModel.update({b1.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(b1.__dict__["age"], 25)
            self.assertIsInstance(b1.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy({bm.id})'))
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestUser(unittest.TestCase):
    """Testing user commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """teardown FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user .
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all user.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cocelia"
            HBNBCommand().onecmd(f'update User {us.id} name "Ace"')
            self.assertEqual(us.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(f'update User {us.id} age 25')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.savings = 25.67
            HBNBCommand().onecmd(f'update User {us.id} savings 35.89')
            self.assertIn("savings", us.__dict__.keys())
            self.assertEqual(us.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'update User {us.id} age 10 color brown'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_destroy_user(self):
        """Test destroy user self
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy User {us.id}')
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestUserDotNotation(unittest.TestCase):
    """Testing the command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """tear down FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test count user self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test all user self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user swelf.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show({us.id})'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, name, "Ace")'))
            self.assertEqual(us.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, age, 25)'))
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update({us.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update({us.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({us.id})'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestState(unittest.TestCase):
    """Testing the  commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """tear down FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all state object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "brown"
            HBNBCommand().onecmd(f'show State {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cocelia"
            HBNBCommand().onecmd(f'update State {st.id} name "Ace"')
            self.assertEqual(st.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(f'update State {st.id} age 25')
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'update State {st.id} age 10 color brown'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(f'destroy State {st.id}')
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestStateDotNotation(unittest.TestCase):
    """Testing the `state` command's dot notation test ceaw
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """teardown FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'State.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_state(self):
        """Test count state object. count
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_state(self):
        """Test all state object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show({st.id})'))
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object self.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, name, "Ace")'))
            self.assertEqual(st.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, age, 25)'))
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'State.update({st.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Test update state object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            cmmd = f'State.update({st.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(st.__dict__["age"], 25)
            self.assertIsInstance(st.__dict__["age"], int)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy({st.id})'))
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestReview(unittest.TestCase):
    """Testing the review commands. unitest
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data.tera"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object. review
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Test all review object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object. review
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "brown"
            HBNBCommand().onecmd(f'show Review {rv.id}')
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cocelia"
            HBNBCommand().onecmd(f'update Review {rv.id} name "Ace"')
            self.assertEqual(rv.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(f'update Review {rv.id} age 25')
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'update Review {rv.id} age 10 color brown)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_destroy_review(self):
        """Test destroy review object.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(f'destroy Review {rv.id}')
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestReviewDotNotation(unittest.TestCase):
    """Testing the `review` command's dot notation unitest
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data tesr soen."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Review.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_review(self):
        """Test count review object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_review(self):
        """Test all review object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show({rv.id})'))
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, name, "Ace")'))
            self.assertEqual(rv.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, age, 25)'))
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'Review.update({rv.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Test update review object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            cmmd = f'Review.update({rv.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(rv.__dict__["age"], 25)
            self.assertIsInstance(rv.__dict__["age"], int)

    def test_destroy_review(self):
        """Test destroy review object.self
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({rv.id})'))
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestPlace(unittest.TestCase):
    """Testing the `place` commands.unittest
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data. teardown"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create place object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_place(self):
        """Test all place object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Place')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "brown"
            HBNBCommand().onecmd(f'show Place {pl.id}')
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Cocelia"
            HBNBCommand().onecmd(f'update Place {pl.id} name "Ace"')
            self.assertEqual(pl.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            HBNBCommand().onecmd(f'update Place {pl.id} age 25')
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'update Place {pl.id} age 10 color brown'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_destroy_place(self):
        """Test destroy place object.self
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(f'destroy Place {pl.id}')
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestPlaceDotNotation(unittest.TestCase):
    """Testing the `place` command's dot notation.unittase
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data. terdown"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create place object. create
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Place.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_place(self):
        """Test count place object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Place:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_place(self):
        """Test all place object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object. show place
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.show({pl.id})'))
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, name, "Ace")'))
            self.assertEqual(pl.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, age, 25)'))
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'Place.update({pl.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_update_place_dict(self):
        """Test update place object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            cmmd = f'Place.update({pl.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(pl.__dict__["age"], 25)
            self.assertIsInstance(pl.__dict__["age"], int)

    def test_destroy_place(self):
        """Test destroy place object.self
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.destroy({pl.id})'))
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestAmenity(unittest.TestCase):
    """Testing the `amenity` commands. unittest
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage datateardown"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create amenity object create
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_amenity(self):
        """Test all amenity object. amenity
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Amenity')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "brown"
            HBNBCommand().onecmd(f'show Amenity {am.id}')
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Cocelia"
            HBNBCommand().onecmd(f'update Amenity {am.id} name "Ace"')
            self.assertEqual(am.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            HBNBCommand().onecmd(f'update Amenity {am.id} age 25')
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'update Amenity {am.id} age 10 color brown)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_destroy_amenity(self):
        """Test destroy amenity object. self
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(f'destroy Amenity {am.id}')
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestAmenityDotNotation(unittest.TestCase):
    """Testing the `amenity` command's dot notation.testcase
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data. teardown"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Amenity.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_amenity(self):
        """Test count amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Amenity:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_amenity(self):
        """Test all amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object. amenityt
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.show({am.id})'))
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, name, "Ace")'))
            self.assertEqual(am.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, age, 25)'))
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'Amenity.update({am.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_update_amenity_dict(self):
        """Test update amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            cmmd = f'Amenity.update({am.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(am.__dict__["age"], 25)
            self.assertIsInstance(am.__dict__["age"], int)

    def test_destroy_amenity(self):
        """Test destroy amenity object.
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.destroy({am.id})'))
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestCity(unittest.TestCase):
    """Testing the `city` commands. contants
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data. teardown"""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create city object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_city(self):
        """Test all city object. self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all City')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object.self
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "brown"
            HBNBCommand().onecmd(f'show City {cty.id}')
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Cocelia"
            HBNBCommand().onecmd(f'update City {cty.id} name "Ace"')
            self.assertEqual(cty.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            HBNBCommand().onecmd(f'update City {cty.id} age 25')
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'update City {cty.id} age 10 color brown'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_destroy_city(self):
        """Test destroy city object.self
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(f'destroy City {cty.id}')
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())


class TestCityDotNotation(unittest.TestCase):
    """Testing the `city` command's dot notation.test
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """tear down FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """create city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'City.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_city(self):
        """Test count city object.great
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == City:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_city(self):
        """Test all city object.purple
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object.object
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "brown"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.show({cty.id})'))
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Cocelia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, name, "Ace")'))
            self.assertEqual(cty.__dict__["name"], "Ace")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, age, 25)'))
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'City.update({cty.id}, age, 10, color, brown)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_update_city_dict(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            cmmd = f'City.update({cty.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(cty.__dict__["age"], 25)
            self.assertIsInstance(cty.__dict__["age"], int)

    def test_destroy_city(self):
        """Test destroy city object.
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.destroy({cty.id})'))
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())
