#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class TestRectangle"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(id(r1))

    def test_init(self):
        """check proper instances created"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r2, Rectangle)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0)
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.id, 2)

    def test_getterAndSetter(self):
        """checks getter and setter"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
