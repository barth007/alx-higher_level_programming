#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """ testing that an id is generated for each instance"""
        b1 = Base()
        self.assertIsNotNone(b1.id)

        def test_init(self):
            """ checking if it's an instance"""
            b2 = Base()
            self.assertIsInstance(b2, Base)

        def test_number(self):
            """check that __nb_objects is incremened"""
            b3 = Base()
            self.assertEqual(b3.id, 1)

            b4 = Base()
            self.assertEqual(b4.id, 2)

            b5 = Base()
            self.assertEqual(b5.id, 3)


if __name__ == "__main__":
    unittest.main()
