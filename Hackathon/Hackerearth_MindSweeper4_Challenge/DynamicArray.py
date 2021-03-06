Dynamic Array
Max. Marks: 20
Sherlock recently learned about dynamic arrays. To test his concepts , Watson asked about few queries about the array.

Queries are defined as follows:

K=1 , Add(x) - add "x" to the dynamic array of numbers.

K=2 , Delete(x) - Delete one occurrence of "x" from the array.

K=3 , smallest(x) - print the 1-based xth smallest element in the array.

K=4 , gcd(L,R) - print the greatest common divisor of all numbers which have occurred between "L" and "R" (both inclusive) in the array.

In delete(x) operation, element "x" is always present in the array. In smallest(x) operation , total number of numbers in the array >= x In gcd(L,R) operation, there will be at least two integers in the range "L" and "R".

Your task is to help Sherlock in answering these queries.

Input:

First contains an integer "Q" which denotes number of queries. Next line is format of queries. It may contain two or three integers separated by single space.

Query format is either "K x" type or "K L R" type.

Output:

Print the answer for those queries which have K=3 or K=4 in a new line for each test case.

Constraints:

1 <= Q <= 10^6
1 <= x <= 10^6
1 <= K <= 4
1 <= L,R <= 10^6
L < R
Sample Input (Plaintext Link)
10
1 2
1 4
1 5
1 6
1 8
3 1
3 5
2 5
4 6 10
4 1 100
Sample Output (Plaintext Link)
2
8
2
2
Explanation
Numbers 2,4,5,6 and 8 are inserted in the array.
For k=3 and x=1, 1st smallest number is 2 in the array.
For k=3 and x=5, 5th smallest number is 8 in the array.
For k=2 and x=5 , number 5 is deleted from the array.
For k=4 , L=6 and R=10 , only 6 and 8 are the numbers which lie in the range from 6 to 10. Hence gcd(6,8) = 2.
For k=4 , L=1 and R=100 , 2,4,6 and 8 are the numbers which lie in the range from 1 to 100. Hence gcd(2,4,6,8 ) = 2.
