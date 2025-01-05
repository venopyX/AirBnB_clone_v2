#!/usr/bin/python3
"""Unittest module for City class."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import MySQLdb
import json
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.city = City()
        cls.city.state_id = "123"
        cls.city.name = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def setUp(self):
        """Set up test method."""
        if storage_type == "db":
            self.db = MySQLdb.connect(
                host=getenv("HBNB_MYSQL_HOST"),
                port=3306,
                user=getenv("HBNB_MYSQL_USER"),
                passwd=getenv("HBNB_MYSQL_PWD"),
                db=getenv("HBNB_MYSQL_DB")
            )
            self.cursor = self.db.cursor()

    def tearDown(self):
        """Clean up test method."""
        if storage_type == "db":
            self.cursor.close()
            self.db.close()

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
        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "San Francisco")

    @unittest.skipIf(storage_type != 'db', "not testing database storage")
    def test_save_db(self):
        """Test save method with DB storage."""
        # Get initial count
        self.cursor.execute("SELECT COUNT(*) FROM cities")
        initial_count = self.cursor.fetchone()[0]

        # Create and save new city
        new_city = City(state_id="456", name="Los Angeles")
        new_city.save()

        # Get new count
        self.cursor.execute("SELECT COUNT(*) FROM cities")
        new_count = self.cursor.fetchone()[0]

        # Verify one record was added
        self.assertEqual(new_count, initial_count + 1)

    @unittest.skipIf(storage_type == 'db', "not testing file storage")
    def test_save_file(self):
        """Test save method with file storage."""
        new_city = City(state_id="789", name="Chicago")
        new_city.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            data = json.load(f)
            key = f"City.{new_city.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]['name'], "Chicago")

    def test_str_representation(self):
        """Test string representation."""
        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(string, str(self.city))

    def test_to_dict_method(self):
        """Test to_dict method."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "123")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
