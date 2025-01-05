#!/usr/bin/python3
"""Unittest module for User class."""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.user = User()
        cls.user.email = "test@example.com"
        cls.user.password = "password123"
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test User initialization."""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_attributes(self):
        """Test User attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_representation(self):
        """Test string representation."""
        string = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(string, str(self.user))

    def test_to_dict_method(self):
        """Test to_dict method."""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
