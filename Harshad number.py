Given an integer N, check whether it is a Harshad number or not.
Note: A Harshad number is an integer, that is divisible by the sum of its digits.

Input Format

First and only line of input contains a integer - N.

Constraints

1 <= N <= 109

Output Format

Print "Yes" if the number is a Harshad number, "No" otherwise.

Sample Input 0

18
Sample Output 0

Yes
...
n=str(input())
s=0
for i in n:
    s=s+int(i)
if (int(n)%s)==0:
    print('Yes')
else:
    print('No')
