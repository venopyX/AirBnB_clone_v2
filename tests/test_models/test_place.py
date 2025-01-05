#!/usr/bin/python3
"""Unittest module for Place class."""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.place = Place()
        cls.place.city_id = "123"
        cls.place.user_id = "456"
        cls.place.name = "My Place"
        cls.place.description = "A nice place"
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 2
        cls.place.max_guest = 6
        cls.place.price_by_night = 100
        cls.place.latitude = 37.7749
        cls.place.longitude = -122.4194
        cls.place.amenity_ids = ["1", "2", "3"]

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test Place initialization."""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_attributes(self):
        """Test Place attributes."""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attribute_types(self):
        """Test Place attribute types."""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attribute_values(self):
        """Test Place attribute values."""
        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "My Place")
        self.assertEqual(self.place.description, "A nice place")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["1", "2", "3"])

    def test_str_representation(self):
        """Test string representation."""
        string = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(string, str(self.place))

    def test_to_dict_method(self):
        """Test to_dict method."""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], "123")
        self.assertEqual(place_dict['user_id'], "456")
        self.assertEqual(place_dict['name'], "My Place")
        self.assertEqual(place_dict['description'], "A nice place")
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertEqual(place_dict['number_bathrooms'], 2)
        self.assertEqual(place_dict['max_guest'], 6)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 37.7749)
        self.assertEqual(place_dict['longitude'], -122.4194)
        self.assertEqual(place_dict['amenity_ids'], ["1", "2", "3"])
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
