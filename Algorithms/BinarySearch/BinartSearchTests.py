

__author__ = 'avimehenwal'


import unittest
from BinarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    """
    BinarySearch TestCases
    """

    def setUp(self):
        self.array = (3, 4, 5, 6, 7, 8, 9)

    def tearDown(self):
        pass

    def test_guess_equals_mid(self):
        guess = 6
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        expected = bs.mid
        self.assertEqual(actual, expected, ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_equals_min(self):
        guess = 3
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        expected = bs.min
        self.assertEqual(actual, expected, ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_equals_max(self):
        guess = 9
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        expected = bs.max
        self.assertEqual(actual, expected, ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_greater_than_max(self):
        guess = 10
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        self.assertTrue(isinstance(actual, Exception), ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_lessthan_min(self):
        guess = 2
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        self.assertTrue(isinstance(actual, Exception), ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_between_mid_and_max(self):
        guess = 8
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        expected = bs.max
        self.assertEqual(actual, expected, ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))

    def test_guess_between_mid_and_min(self):
        guess = 4
        bs = BinarySearch(self.array, guess)
        actual = bs.do_binary_search()
        expected = bs.mid
        self.assertEqual(actual, expected, ("actual={} iter={} expected={}".format(actual, bs.iter, expected)))


if __name__ == '__main__':
    TestBinarySearch()


