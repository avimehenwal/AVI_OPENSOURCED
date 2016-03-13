"""
Lucky numbers are defined as the numbers consisting only of digits 3 and 5. So, given a number N, you have to print the least lucky number strictly greater than N.

Input:
First line of input contains number of test cases T. Each test case contains a single number N.

Output:
For each test case, print the next lucky number in a separate line.

Constraints:
1<=T<=1000 
1<=N<=10100

4      5
4      33
48     53
130    333
98     333

####################### ToDo : Combinotorics
import itertools
n=int(input())
for i in range(n):
	l=[]
	k=int(input())
	c=len(str(k))
	for i in range(c):
		l.append(3)
		l.append(5)
	a=[]	
	for i in itertools.permutations(l,c):
		s=''
		for j in i:
			s+=str(j)
		a.append(s)
	
	a=sorted(set(a))
	f=0
	if(int(a[-1])>k):
		for i in a:
			if(int(i)>k):
				f=1
				print(i)
				break
		
	if(f==0):
		print('3'*(c+1))	
"""

n = raw_input()
N = int(n)
print '%s %s' % (type(n), type(N))
if not N <= 10100 and N >= 1:
    break

def ln_gen(ln):
    """ takes length and returns lucky numbers """
    lucky_no = ('3', '5')
    for i in ln:
        for n in lucky_no:
            yield n



ln = len(n)


if not T <=1000 and T >= 1:
    break
