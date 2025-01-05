#!/usr/bin/python3
"""Unittest module for State class."""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for State class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test State initialization."""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_attributes(self):
        """Test State attributes."""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_types(self):
        """Test State attribute types."""
        self.assertIsInstance(self.state.name, str)

    def test_attribute_values(self):
        """Test State attribute values."""
        self.assertEqual(self.state.name, "California")

    def test_str_representation(self):
        """Test string representation."""
        string = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(string, str(self.state))

    def test_to_dict_method(self):
        """Test to_dict method."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "California")
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
