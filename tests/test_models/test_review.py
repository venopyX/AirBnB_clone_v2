#!/usr/bin/python3
"""Unittest module for Review class."""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.review = Review()
        cls.review.place_id = "123"
        cls.review.user_id = "456"
        cls.review.text = "Great place to stay!"

    @classmethod
    def tearDownClass(cls):
        """Clean up test class."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test Review initialization."""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_attributes(self):
        """Test Review attributes."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """Test Review attribute types."""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attribute_values(self):
        """Test Review attribute values."""
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great place to stay!")

    def test_str_representation(self):
        """Test string representation."""
        string = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(string, str(self.review))

    def test_to_dict_method(self):
        """Test to_dict method."""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great place to stay!")
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_datetime_attributes(self):
        """Test datetime attributes."""
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
