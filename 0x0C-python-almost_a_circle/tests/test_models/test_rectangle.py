#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


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

    def test_for_error(self):
        """tests input to raise error messages"""
        r = Rectangle(30, 70)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "20"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "40"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -50
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = "20"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -20
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "30"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -30

    def test_area(self):
        """Tests input to compute with area method"""
        r1 = Rectangle(6, 8)
        self.assertEqual(r1.area(), 48)
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)

    def test_display(self):
        """testing the display method"""
        r3 = Rectangle(3, 5)
        buffer_output = StringIO()
        sys.stdout = buffer_output
        r3.display()
        sys.stdout = sys.__stdout__
        output_contents = buffer_output.getvalue()
        self.assertEqual(output_contents, "###\n###\n###\n###\n###\n")


if __name__ == "__main__":
    unittest.main()
