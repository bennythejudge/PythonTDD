import unittest
from simple import greet

class TestSimple(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("John"), "Hi, John.")
