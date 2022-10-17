Given a string, check if it contains only vowels.

Input Format

Input contains a string S, consisting of lowercase and uppercase characters.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only vowels, "No" Otherwise.

Sample Input 0

SmartInterviews
Sample Output 0

No
...
s=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    if i not in v:
        c=c+1
if c==0:
    print("Yes")
else:
    print("No")
