#!/usr/bin/env python

# PURPOSE   : Read a big file in chunks
# AUTHOR    : avimehenwal
# DATE      : 06-jan-2015

""" Next Lucky Number
Lucky numbers are defined as the numbers consisting only of digits 3 and 5. So, given a number N, you have to print the least lucky number strictly greater than N.

Input:
First line of input contains number of test cases T. Each test case contains a single number N.

Output:
For each test case, print the next lucky number in a separate line.

Constraints:
1<=T<=1000
1<=N<=10100

Sample Input (Plaintext Link)
4
4
48
130
98

Sample Output (Plaintext Link)
5
53
333
333
"""

# SOLUTION

import itertools

class LuckyNumber(object):

    def __init__(self, n):
        # n = input()
        self.n = str(n)
        self.digits = len(self.n)
        self.N = int(self.n)
        # print("No of digits in %s = %s" % (self.n, self.digits))
        self.main()

    def get_product(self, repeat):
        self.product = list(itertools.product([3, 5], repeat=repeat))
        # print(self.product)
        return self.product
        # print(self.product[0][0])
        # print(type(self.product[0][0]))

    def make_int(self, tup):
        """ makes a integer from the tuple """
        # elements inside tuple should be str for join TypeError
        # print(tup)
        nu = int(''.join(str(x) for x in tup))
        # print(nu)
        return nu

    def greaterno(self, nu_list, N):
        """ returns the greater no from sorted list """
        for number in nu_list:
            if number > N:
                return number
        # No greater no strictly greater no found in range
        return False

    def main(self):
        nu_list = [self.make_int(item) for item in self.get_product(self.digits) ]
        # print(nu_list)
        sorted_nu_list = sorted(nu_list)
        # print(sorted_nu_list)
        lucky_no = self.greaterno(sorted_nu_list, self.N)
        if not lucky_no:
            self.increment = self.digits + 1
            nu_list = [self.make_int(item) for item in self.get_product(self.increment) ]
            # print(nu_list)
            sorted_nu_list = sorted(nu_list)
            # print(sorted_nu_list)
            lucky_no = self.greaterno(sorted_nu_list, self.N)
        # print("lucky_no for %s = %s" % (self.n, lucky_no))
        print(lucky_no)

# MAIN
if __name__ == "__main__":

    LuckyNumber('4')
    LuckyNumber('48')
    LuckyNumber('130')
    LuckyNumber('98')

