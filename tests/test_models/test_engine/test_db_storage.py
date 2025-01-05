#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
import MySQLdb
DBStorage = db_storage.DBStorage
classes = {
    "Amenity": Amenity, "City": City, "Place": Place,
    "Review": Review, "State": State, "User": User
}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/'
                                  'test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                        "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                       "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                        "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                       "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                            "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                          "{:s} method needs a docstring".format(func[0]))


@unittest.skipIf(storage_t != 'db', "not testing db storage")
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    
    def setUp(self):
        """Set up test environment"""
        self.db = MySQLdb.connect(
            host=os.getenv("HBNB_MYSQL_HOST"),
            port=3306,
            user=os.getenv("HBNB_MYSQL_USER"),
            passwd=os.getenv("HBNB_MYSQL_PWD"),
            db=os.getenv("HBNB_MYSQL_DB")
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Clean up test environment"""
        self.cursor.close()
        self.db.close()

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        # Get all objects
        all_objs = models.storage.all()
        
        # Count objects in database
        count = 0
        for table in ['amenities', 'cities', 'places', 
                     'reviews', 'states', 'users']:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count += self.cursor.fetchone()[0]
            
        self.assertEqual(len(all_objs), count)

    def test_new(self):
        """Test that new adds an object to the database"""
        # Create a new state
        state = State(name="California")
        
        # Get initial count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]
        
        # Add and save the state
        models.storage.new(state)
        models.storage.save()
        
        # Get new count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]
        
        # Verify one record was added
        self.assertEqual(new_count, initial_count + 1)

    def test_save(self):
        """Test that save properly saves objects to the database"""
        # Create a new state
        state = State(name="Texas")
        
        # Get initial count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]
        
        # Add and save the state
        models.storage.new(state)
        models.storage.save()
        
        # Get new count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]
        
        # Verify one record was added
        self.assertEqual(new_count, initial_count + 1)
        
        # Verify the data was saved correctly
        self.cursor.execute("SELECT name FROM states WHERE id=%s", (state.id,))
        result = self.cursor.fetchone()
        self.assertEqual(result[0], "Texas")


if __name__ == '__main__':
    unittest.main()
