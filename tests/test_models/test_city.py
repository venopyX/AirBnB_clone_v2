#!/usr/bin/python3
"""Unittest module for City class."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def setUp(self):
        """Set up test environment."""
        self.city = City()

    def tearDown(self):
        """Clean up test environment."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test City initialization."""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test City attributes."""
        # SQLAlchemy models have nullable=False, so these might be None initially
        self.assertIsNone(self.city.state_id)
        self.assertIsNone(self.city.name)

    def test_attributes_assignment(self):
        """Test City attribute assignment."""
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_to_dict_method(self):
        """Test to_dict method."""
        # Set required attributes first
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "San Francisco")


if __name__ == "__main__":
    unittest.main()
