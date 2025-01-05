#!/usr/bin/python3
"""Unittest module for Amenity class."""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.amenity = Amenity()
        cls.amenity.name = "Swimming Pool"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test Amenity initialization."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_str_representation(self):
        """Test string representation."""
        string = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(string, str(self.amenity))

    def test_to_dict_method(self):
        """Test to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "Swimming Pool")
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
