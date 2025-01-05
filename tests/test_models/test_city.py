#!/usr/bin/python3
"""Unittest module for City class."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.city = City()
        cls.city.state_id = "CA"
        cls.city.name = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test City initialization."""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_attributes(self):
        """Test City attributes."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_str_representation(self):
        """Test string representation."""
        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(string, str(self.city))

    def test_to_dict_method(self):
        """Test to_dict method."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
