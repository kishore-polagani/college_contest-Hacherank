Given a string, check if it contains only digits.

Input Format

Input contains a string S, consisting of ascii characters.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only digits, "No" otherwise.

Sample Input 0

123456786543
Sample Output 0

Yes
...
s=input()
x=['0','1','2','3','4','5','6','7','8','9']
c=0
for i in s:
    if i in x:
        c=c+1
        
if c==len(s):
    print("Yes")
else:
    print("No")
