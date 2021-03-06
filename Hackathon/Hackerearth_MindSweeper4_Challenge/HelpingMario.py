#!/usr/bin/env python

# Hackathon Mindsweeper4
# AUTHOR  : avimehenwal
# DATE    : 06-Jan-2014

""" PROBLEM
Helping Mario
Max. Marks: 15

Mario loved his girlfriend Lucy very much. Michael was jealous of Mario's love. So, he kidnapped Lucy. Mario started searching for her and found a note which was written by Michael. In that note, Michael asked Mario to solve a problem if he wanted his girlfriend back. The note had the following problem. Given some numbers , Mario had to find the number of subsequences such that the greatest common divisor of all numbers in subsequence lies between "L" and "R"(both inclusive).

Mario asked your help to solve the problem.

Note: A sub-sequence can be obtained from the original sequence by deleting 0 or more integers from the original sequence.

Input:

First line contains an integer "t" , denoting the number of testcases. First line of each test has an integer "N". Second line contains "N" space separated integers. Third line contains two integers "L" and "R".

Output:

Print the answer of above described problem in a new line for each testcase.

Constraints:

1 <= t <= 1000
1 <= N <= 50
1 <= numbers <= 10^5
1 <= L,R <= 100
L <= R
All numbers will be distinct

Sample Input (Plaintext Link)
2
2
1 2
1 2
1
1
1 100
Sample Output (Plaintext Link)
3
1
Explanation
For 1st testcase, possible subsequences are {1},{2},{1,2}.
Possible greatest common divisors are 1 and 2. Hence the answer is 3.

For 2nd testcase, possible subsequences are {1}.
Possible greatest common divisor is only 1. Hence the answer is 1.
Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed languages: C, C++, Java, Python
"""

