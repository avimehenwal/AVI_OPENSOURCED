"""
Minimizing Path Cost
Max. Marks 100
In India, there are many railway stations. There's no way you could avoid one. So, the protagonist in our problem is given N railway stations and M direct two way connections for these railway stations. Let us say that we connect railway station u and v directly - that is to say, you can go from u to v directly without passing any other station.

You have been hired by the Indian Railways (Congratulations!) to compute the shortest path between two railway stations, so that they can minimize the time taken to travel between those stations. M direct connections will be of the following form: Station1 Station2 D, this means there is a direct connection between Station1 and Station2 and there's a distance of D Kilometers.

Keep in mind that each train takes 1 minute to travel 1 km. The stoppage time is too small, and thus can be ignored.

You will be given Q queries of type Source Destination. You have to find the shortest path from Source to Destination.

Input:

First line of input contains two integers N and M denoting number of railway stations and number of direct connections respectively.
Next line contains N strings denoting the name of the stations.
Next M lines contains two strings Station1, Station2 and an integer D denoting that there is a direct connection between Station1 and Station2 having D distance between them.
Next line contains a single integer Q denoting number of queries.
Next Q lines contain two strings Source and Destination.

Output:
For each query output a single integer denoting the cost of the shortest path between source and destination.

Constraints:
1 <=N <= 100
1 <= M <= N * (N - 1) / 2
1 <= Q <= N * (N - 1) / 2

Sample Input (Plaintext Link)
4 4
Howrah Trivandram Vashi Mysore
Howrah Trivandram 10
Howrah Vashi 20
Trivandram Mysore 100
Mysore Vashi 50
6
Howrah Trivandram
Howrah Vashi
Howrah Mysore
Trivandram Vashi
Trivandram Mysore
Mysore Vashi
Sample Output (Plaintext Link)
10
20
70
30
80
50
Explanation
For query 1 : Minimum Cost path is Howrah -> Trivandram of total length 10.
For query 2 : Minimum Cost path is Howrah -> Vashi of total length 20.
For query 3 : Minimum Cost path is Howrah -> Vashi -> Mysore of total length 20 + 50 = 70.
For query 4 : Minimum Cost path is Trivandram -> Howrah -> Vashi of total length 10 + 20 = 30.
For query 5 : Minimum Cost path is Trivandram -> Howrah -> Vashi -> Mysore of total length 10 + 20 + 50 = 80.
For query 6 : Minimum Cost path is Mysore -> Vashi of total length 50.
"""