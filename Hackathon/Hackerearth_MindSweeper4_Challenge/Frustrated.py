Frustrated
Max. Marks: 20
ARE U A MATHEMATICAL PRODIGY OR A BIG INT USER OR THE HOLY DYNAMIC PROGRAMMER ?

Given two natural numbers , X and Y. Find the largest prime number less than or equal to K which is a subsequence of both A and B.

Subsequence of two numbers A and B is defined same as that of two strings if digits were to be treated as characters.
there won't be any leading zeros in K , X , Y
If you get stuck , remember , that memory is a lot cheaper than processing power.

"Most tests in our life are repetitive. Those who don't learn from one test of life, are bound to repeat the same test again and again. and this slows them down"

NOTE: The test cases are not all distinct.

INPUT FORMAT :

The first line of Input file starts with T, number of test case. the following T lines contains test cases, each have K,X,Y in the respective order.

OUTPUT FORMAT:

Output T lines, each containing the largest prime number less than or equal to K which is a subsequence of both A and B.

If no solution exists, then print -1.

INPUT CONSTRAINTS :

1 <= T <= 10^4
1 <=X <= 10^100
1 <=Y <= 10^100
1 <= K <= 10^6
Sample Input (Plaintext Link)
2
10 1231423423423 1098509489729
18 111111111111111111111117 998989766786817862364727
Sample Output (Plaintext Link)
2
17
Explanation
In the first sample testcase, we need largest prime number which is less than or equal to 10. There are 2,3,5 and 7 as candidates. 3,5 and 7 are not common to the sample strings X and Y. So our answer is 2.

In second one , we need largest prime which is less than or equal to 18 and can be a common sequences of strings X and Y. 17 is the answer.
Time Limit: 2 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed languages: C, C++, Java, Python
