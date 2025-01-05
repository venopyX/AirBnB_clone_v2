#!/usr/bin/python3
"""Unittest module for BaseModel class."""
import unittest
import os
import json
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up test environment."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test BaseModel initialization."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        expected_format = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_format)

    def test_save_method(self):
        """Test save method updates updated_at."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns correct dictionary."""
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_kwargs_init(self):
        """Test initialization with keyword arguments."""
        base_dict = self.base_model.to_dict()
        new_model = BaseModel(**base_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.base_model.id)
        self.assertEqual(new_model.created_at, self.base_model.created_at)


if __name__ == "__main__":
    unittest.main()
