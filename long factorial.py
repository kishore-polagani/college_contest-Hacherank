Given a non-negative number - N, print N!

Input Format

First and only line of input contains a number - N.

Constraints

0 <= N <= 20

Output Format

Print factorial of N.

Sample Input 0

3
Sample Output 0

6
..
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)
