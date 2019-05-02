import unittest
import functions

class TestFunctions(unittest.TestCase):
    def test_double(self):
        self.assertEqual(functions.double(0), 0)
        self.assertEqual(functions.double(1), 2)
        self.assertEqual(functions.double(-10), -20)
