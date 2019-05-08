import unittest
import misc


class TestFunctions(unittest.TestCase):

    def test_double(self):
        self.assertEqual(misc.double(0), 0)
        self.assertEqual(misc.double(1), 2)
        self.assertEqual(misc.double(7), 14)
        self.assertEqual(misc.double(-10), -20)

    def test_convert_to_str(self):
        self.assertEqual(misc.convert_to_str(0), "0")
        self.assertEqual(misc.convert_to_str(1), "1")
        self.assertEqual(misc.convert_to_str(7), "7")
        self.assertEqual(misc.convert_to_str(-10), "-10")

    def test_sum_list(self):
        self.assertEqual(misc.sum_list([0]), 0)
        self.assertEqual(misc.sum_list([1]), 1)
        self.assertEqual(misc.sum_list([1, 2, 3, 1]), 7)
        self.assertEqual(misc.sum_list([1, -1, 10, -10, -5, -2, -3]), -10)

    def test_multiply_list(self):
        self.assertEqual(misc.multiply_list([0]), 0)
        self.assertEqual(misc.multiply_list([1]), 1)
        self.assertEqual(misc.multiply_list([-1]), -1)
        self.assertEqual(misc.multiply_list([1, 2, 3, 1]), 6)
        self.assertEqual(misc.multiply_list([0, 4]), 0)
        self.assertEqual(misc.multiply_list([-2, -5]), 10)
        self.assertEqual(misc.multiply_list([-2, 5]), -10)
        self.assertEqual(misc.multiply_list(
            [1, -1, 10, -10, -5, -2, -3]), -3000)

    def test_find_max(self):
        self.assertEqual(misc.find_max([0]), 0)
        self.assertEqual(misc.find_max([1]), 1)
        self.assertEqual(misc.find_max([-1]), -1)
        self.assertEqual(misc.find_max([1, 2, 3, 1]), 3)
        self.assertEqual(misc.find_max([0, 4]), 4)
        self.assertEqual(misc.find_max([-2, -5]), -2)
        self.assertEqual(misc.find_max([-2, 5]), 5)
        self.assertEqual(misc.find_max(
            [1, -1, 10, -10, -5, -2, -3]), 10)
