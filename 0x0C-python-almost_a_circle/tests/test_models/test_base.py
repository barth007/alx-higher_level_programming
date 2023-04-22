#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class TestBase"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        """check instance"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)
