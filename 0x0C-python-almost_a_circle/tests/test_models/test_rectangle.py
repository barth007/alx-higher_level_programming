#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class TestRectangle"""
    def test_constructor(self):
        """testing constructor"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)
        r2 = Rectangle(30, 50, 74, 40, 80)
        self.assertEqual(r2.width, 30)
        self.assertEqual(r2.height, 50)
        self.assertEqual(r2.x, 74)
        self.assertEqual(r2.y, 40)
        self.assertEqual(r2.id, 80)

    def test_getters_setters(self):
        """test getter and setter method"""
        r = Rectangle(10, 30)
        r.width = 30
        self.assertEqual(r.width, 30)
        r.height = 49
        self.assertEqual(r.height, 49)
        r.x = 60
        self.assertEqual(r.x, 60)
        r.y = 50
        self.assertEqual(r.y, 50)


if __name__ == "__main__":
    unittest.main()
