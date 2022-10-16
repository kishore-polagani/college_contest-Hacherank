Given an integer N, check whether it is a Narcissistic number or not.
Note: A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

Input Format

First and only line of input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Narcissistic number, "No" otherwise.

Sample Input 0

8208
Sample Output 0

Yes
...

n=str(input())
l=len(n)
s=0
for i in n:
    s=s+int(i)**l
if s==int(n):
    print("Yes")
else:
    print("No")
