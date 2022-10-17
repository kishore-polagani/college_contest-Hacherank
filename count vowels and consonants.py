Given a string, print count of vowels and consonants in the string.

Input Format

Input contains a string S, consisting of lowercase and uppercase characters.

Constraints

1 <= len(S) <= 100

Output Format

Print count of vowels and consonants in the given string, separated by space.

Sample Input 0

aBxbbiAasPw
Sample Output 0

4 7
...
n=input()
c=0
s=0
x=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in x:
        c=c+1
    else:
        s=s+1
print(c,end=" ")
print(s)
