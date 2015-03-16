#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '16-March-2015'
__purpose__ = 'Binary Search Implementation with python'

"""
Input: Ordered array
Output: Search
Test
"""

class BinarySearch():
    """
    Binary Seach Implementation via python Tuples used as Arrays
    """

    def __init__(self, array, guess):
        self.iter = 0
        self.array = array
        self.guess = guess
        self.min = 0
        try:
            self.do_input_validation()
        except Exception as e:
            self.error = e
            print("Exitting: %s" % self.error)
        self.max = len(array) - 1
        self.mid = (self.min + self.max ) // 2

    def ordered_array_or_not(self, array):
        pass

    def do_binary_search(self):
        while True:
            self.iter += 1
            if self.max < self.min:
                return -1
            self.mid = (self.min + self.max) // 2
            if self.array[self.mid] < self.guess:
                self.min = self.mid + 1
            elif self.array[self.mid] > self.guess:
                self.max = self.mid - 1
            else:
                return self.mid

    def do_input_validation(self):
        if not isinstance(self.array, tuple):
            raise TypeError("%s not Tuple Type" % self.array)
        if not isinstance(self.guess, int):
            raise TypeError("%s not Integer Type" % self.guess)





