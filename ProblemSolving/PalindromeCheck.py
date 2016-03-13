#!/usr/bin/env python

__author__  = 'avimehenwal'
__date__    = '13-March-2016'
__purpose__ = 'Palindrome Check'


"""
Check if a palindrome could be genearted from a given string or not
"""

def is_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    else:
        return False

if __name__ == '__main__':
    strings = ['avi', 'avva', 'f', 'ds', 'gg', 'misssisssim', 'missisippy']
    for string in strings:
        if is_palindrome(string):
            print string, 'is PALINDROME'
        else:
            print string, 'is NOT palindrome'

