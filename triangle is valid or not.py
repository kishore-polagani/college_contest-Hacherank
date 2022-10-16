Given the length of 3 sides of a triangle, check whether the triangle is valid or not.

Input Format

First and only line of input contains three integers A, B, C - length of sides of the triangle.

Constraints

1 <= A, B, C <= 109

Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.

Sample Input 0

4 3 5
Sample Output 0

Yes
...
x=list(map(int,input().split()))
y=x[0]
z=x[1]
p=x[2]
if ((y+z)<=p) or ((z+p)<=y) or ((p+y)<=z):
    print("No")
else:
    print("Yes")
