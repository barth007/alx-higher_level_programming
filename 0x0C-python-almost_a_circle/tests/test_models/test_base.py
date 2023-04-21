#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """creates three instances of the Base"""
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(id=10)

    def test_id(self):
        """ testing that an id is generated for each instance"""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 10)

        def test_package(self):
            """ test if it's a package"""
            self.assertEqual(models.__name__, 'models')
            self.assertInstance(models, type(__builtins__))


if __name__ == "__main__":
    unittest.main()
